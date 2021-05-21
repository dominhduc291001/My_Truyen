from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Truyen(models.Model):
    IDtruyen = models.CharField(max_length = 30, primary_key = True)
    tentruyen = models.CharField(max_length = 100)
    tacgia = models.CharField(max_length = 100)
    nguon = models.CharField(max_length = 100)
    trangthai = models.BooleanField(default = False)
    yeuthich = models.IntegerField(default = 0)
    luotxem = models.IntegerField(default=0)
    gioithieu = models.TextField(max_length = 5000 )
    anh = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.tentruyen} "

class Theloai(models.Model):
    IDtheloai= models.CharField(max_length=50, primary_key= True)
    tentheloai =  models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tentheloai} "

class Chaptruyen(models.Model):
    IDtruyen = models.ForeignKey(Truyen, on_delete=models.CASCADE)
    chap = models.IntegerField(default=0)
    tenchap = models.CharField(max_length=100)
    noidung = RichTextField(blank = True, null= True)
    thoigian = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.IDtruyen.pk} - Chap {self.chap} : {self.tenchap} "

class Checktheloai(models.Model):
    IDtheloai = models.ForeignKey(Theloai, on_delete=models.CASCADE)
    IDtruyen = models.ForeignKey(Truyen, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.IDtruyen.pk} : {self.IDtheloai.pk} "

class Theodoi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    IDtruyen = models.ForeignKey(Truyen, on_delete=models.CASCADE)

