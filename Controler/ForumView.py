from django.shortcuts import render
from Data.models import Profile
from Data.models import Post
from django.views.generic import ListView, DetailView, CreateView
from Data.formResgister import PostForm

class ForumView(ListView):
    model = Post
    template_name = 'Forum/forum.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Forum/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Forum/add_post.html'
    #fields = '__all__'

