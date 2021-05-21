from django.contrib import admin
from .models import *
# Register your models here.

myModels = [Truyen,Theloai, Checktheloai,Chaptruyen,Theodoi]
admin.site.register(myModels)