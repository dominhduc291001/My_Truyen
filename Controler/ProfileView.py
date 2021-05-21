from django.shortcuts import render, get_object_or_404
from Data.models import Profile
from Data.models import Post
from django.views.generic import ListView, DetailView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
#from .forms import EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'Profile/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']
    success_url = reverse_lazy('Home Page')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'Profile/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
