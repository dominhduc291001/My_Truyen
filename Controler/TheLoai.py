from django.shortcuts import render
from Data.models import Truyen, Chaptruyen
from Data.models import Checktheloai
from Data.models import Theloai

def TheLoai(request,id):
    content = {"listTheLoai":getTruyen(id)}
    return render(request,"TheLoai/index.html",content)

def getTruyen(idTheLoai):
    listTruyen = Checktheloai.objects.filter(IDtheloai=idTheLoai)
    temp = []
    res = []
    for item in listTruyen:
        temp.append(item.IDtruyen.pk)
    fullTruyen = Truyen.objects.all()
    for truyen in fullTruyen:
        for p in temp:
            if truyen.IDtruyen == p:
                res.append(truyen)
    return res