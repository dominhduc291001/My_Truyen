from django.db import models
from ckeditor.fields import RichTextField

class Truyen(models.Model):
    IDtruyen = models.CharField(max_length = 30, primary_key = True)
    tentruyen = models.CharField(max_length = 100)
    tacgia = models.CharField(max_length = 100)
    nguon = models.CharField(max_length = 100)
    trangthai = models.BooleanField(default = False)
    yeuthich = models.IntegerField(default = 0)
    luotxem = models.IntegerField(default=0)
    gioithieu = models.CharField(max_length = 5000 )
    anh = models.ImageField(upload_to='images/')

class Theloai(models.Model):
    IDtheloai= models.CharField(max_length=50, primary_key= True)
    tentheloai =  models.CharField(max_length=100)

class Chaptruyen(models.Model):
    IDtruyen = models.ForeignKey(Truyen, on_delete=models.CASCADE)
    chap = models.IntegerField(default=0)
    tenchap = models.CharField(max_length=100)
    noidung = RichTextField(blank = True, null= True)
    #thoigian = models.DateTimeField(auto_now= True)

class Checktheloai(models.Model):
    IDtheloai = models.ForeignKey(Theloai, on_delete=models.CASCADE)
    IDtruyen = models.ForeignKey(Truyen, on_delete=models.CASCADE)


