from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from account.models import Follow
from .models import Tweet
from .forms import TweetForm


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class AjaxListView(ListView):
	context_object_name = 'items'
	paginate_by = 6

	def render_to_response(self, context):
		if self.request.is_ajax():
			self.template_name = 'tweets/list_ajax.html'
			return super(AjaxListView, self).render_to_response(context)
		else:
			return super(AjaxListView, self).render_to_response(context)


class AllTweetsListView(AjaxListView):
	model = Tweet
	template_name = 'tweets/list.html'


class UserFeedListView(LoginRequiredMixin, AjaxListView):
	model = Tweet 
	template_name = 'tweets/list.html'

	def get_queryset(self):
		queryset = Tweet.objects.all()
		following_ids = self.request.user.following.values_list('id', flat=True)
		queryset = queryset.filter(user_id__in=following_ids) 
		return queryset


class UserPageListView(AjaxListView):
	model = Tweet
	template_name = 'tweets/user_page.html'

	def get_queryset(self):
		username = self.kwargs.pop('username', None)
		self.user = get_object_or_404(User, username=username)
		queryset = Tweet.objects.filter(user=self.user.id)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(UserPageListView, self).get_context_data(**kwargs)
		context['user'] = self.user 
		return context


class NewTweetView(LoginRequiredMixin, FormView):
	template_name = 'tweets/new_tweet.html'
	form_class = TweetForm
	success_url = '/'

	def form_valid(self, form):
		new_tweet = form.save(commit=False)
		new_tweet.user = self.request.user 
		new_tweet.save()
		return super(NewTweetView, self).form_valid(form)


@login_required
@require_POST
def follow(request):
	user_id = request.POST.get('id')
	action = request.POST.get('action')
	if user_id and action:
		try:
			user = User.objects.get(id=user_id)
			if action == 'follow':
				Follow.objects.get_or_create(
					user_from=request.user,
					user_to=user)
			else:
				Follow.objects.filter(
					user_from=request.user,
					user_to=user).delete()
			return JsonResponse({'status': 'ok'})
		except User.DoesNotExist:
			return JsonResponse({'status': 'ko'})
	return JsonResponse({'status': 'ko'})