from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from Data.Form.accountForm import EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('Home Page')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('Home Page')

    def get_object(self):
        return self.request.user

