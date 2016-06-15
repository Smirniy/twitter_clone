from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, \
									PageNotAnInteger
from account.models import Follow
from .models import Tweet
from .forms import TweetForm

def ajax_scroll(request, items, list_page, ajax_page, **values):
	context = {}
	paginator = Paginator(items, 6)
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		items = paginator.page(paginator.num_pages)
	context['items'] = items
	context.update(**values)
	if request.is_ajax():
		return render(request,
					ajax_page,
					context)
	return render(request,
					list_page,
					context)

def all_tweets(request):
	tweets = Tweet.objects.all()
	list_page = 'tweets/list.html'
	ajax_page = 'tweets/list_ajax.html'
	return ajax_scroll(request, tweets, list_page, ajax_page)

@login_required
def user_feed(request):
	tweets = Tweet.objects.all()
	following_ids = request.user.following.values_list('id', flat=True)
	tweets = tweets.filter(user_id__in=following_ids) 
	list_page = 'tweets/list.html'
	ajax_page = 'tweets/list_ajax.html'
	return ajax_scroll(request, tweets, list_page, ajax_page)
	

def user_page(request, username):
	user = get_object_or_404(User, username=username)
	tweets = Tweet.objects.filter(user=user.id)
	list_page = 'tweets/user_page.html'
	ajax_page = 'tweets/list_ajax.html'
	return ajax_scroll(request, tweets, list_page, ajax_page, user=user)

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



@login_required
def new_tweet(request):
	if request.method == 'POST':
		form = TweetForm(data=request.POST)
		if form.is_valid():
			new_tweet = form.save(commit=False)
			new_tweet.user = request.user 
			new_tweet.save()
			return redirect("/")
	else:
		form = TweetForm()
	return render(request,
		'tweets/new_tweet.html',
		{'form': form})
