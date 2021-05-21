from django.shortcuts import render
from Data.models import Truyen, Chaptruyen
from Data.models import Checktheloai
from Data.models import Theloai

def ChapView(request,idTruyen,id):
    myTruyen = Truyen.objects.get(IDtruyen= idTruyen)
    myChap = Chaptruyen.objects.get(id = id)
    content = {"myTruyen":myTruyen,
               "myChap":myChap}
    return render(request,"ChapView/index.html",content)