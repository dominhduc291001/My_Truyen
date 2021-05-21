from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.

class TruyenAdmin (ModelAdmin):

    ordeing=['IDtruyen']
    list_display=['IDtruyen','tentruyen','luotxem','trangthai','tacgia','nguon']
    list_per_page=10
    list_display_links=['IDtruyen','tentruyen']
    list_editable=['trangthai']
    search_fields = ('IDtruyen','tentruyen','tacgia',)

class TheLoaiAdmin (ModelAdmin) :
    ordeing = ['IDtheloai']
    list_display =['IDtheloai','tentheloai']
    list_per_page = 10
    search_fields=('IDtheloai','tentheloai')

class ChapTruyenAdmin (ModelAdmin) :
    ordeing=['IDtruyen']
    list_display=['IDtruyen','chap','tenchap']
    search_fields = ('IDtruyen','chap')
    list_filter=['IDtruyen']
class CheckTheLoaiAdmin (ModelAdmin) :
    ordeing = ['IDtheloai']
    list_editable=['IDtruyen']
    list_display=['IDtheloai','IDtruyen']
myModels = [Truyen,Theloai, Checktheloai,Chaptruyen,TheLoaiAdmin,CheckTheLoaiAdmin,ChapTruyenAdmin,TruyenAdmin]
admin.site.register(myModels)
