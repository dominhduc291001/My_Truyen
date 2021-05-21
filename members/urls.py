from django.urls import path
from .views import UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name="password"),
    path('password_success', views.password_success, name="password_success"),
]