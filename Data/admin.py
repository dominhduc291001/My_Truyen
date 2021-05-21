from django.contrib import admin
from .models import *
from .models import Profile
from .models import Post
# Register your models here.

myModels = [Truyen,Theloai, Checktheloai,Chaptruyen,Theodoi]
admin.site.register(myModels)
admin.site.register(Profile)
admin.site.register(Post)