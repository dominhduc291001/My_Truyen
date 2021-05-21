"""MyTruyen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Home, name='Home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='Home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Controler.ForumView import ForumView, ArticleDetailView, AddPostView
from Controler.ProfileView import ShowProfilePageView, EditProfilePageView

import Controler.AuthView
from Controler.HomeView import home

from Controler.SelectTruyen import SelectTruyen
from Controler.ChapView import ChapView

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='Home Page'),
    path('register/', Controler.AuthView.registerPage, name='register'),
    path('logout/', Controler.AuthView.logoutUser, name='logout'),
    path('login/', Controler.AuthView.loginPage, name='login'),
    path('SelectTruyen/<str:id>/',SelectTruyen,name='SelectTruyen'),
    path('chap/<str:idTruyen>/<int:id>/',ChapView,name='ChapView'),

    path('edit_profile_page/<int:pk>', EditProfilePageView.as_view(), name="edit_profile_page"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('forum/', ForumView.as_view(), name="forum"),
    path('members/', include('members.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)