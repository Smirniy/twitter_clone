from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.views.generic.edit import CreateView

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.set_password(form.cleaned_data['password'])
        instance.save()
        profile = Profile.objects.create(user=instance)
        return render(self.request, 'account/register_done.html')

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated')
        else:
            messages.error(request, 'Error updating profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})


