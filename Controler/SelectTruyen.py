from django.shortcuts import render
from Data.models import Truyen, Chaptruyen
from Data.models import Checktheloai
from Data.models import Theloai



def SelectTruyen(request,id):
    myTruyen = Truyen.objects.get(IDtruyen = id)
    myTruyen.luotxem += 1
    myTruyen.save()
    content = {"myTruyen":myTruyen,
               "theLoai":getTheLoai(id),
               "newChap":getNewChap(id),
               "allChap":getAllChap(id),
               "sameType":getSameType(id),
               "numberChap":getNumberChap(id),
               "firstChap":getFirstChap(id)}
    return render(request,"SelectTruyen/index.html",content)
def getTheLoai(id):
    myTruyen = Truyen.objects.get(IDtruyen=id)
    listTheLoai = Checktheloai.objects.filter(IDtruyen=myTruyen.IDtruyen)
    temp = []
    res = ""
    for item in listTheLoai:
        temp.append(item.IDtheloai.pk)
    fullTheLoai = Theloai.objects.all()
    for theloai in fullTheLoai:
        for p in temp:
            if theloai.IDtheloai == p:
                res += theloai.tentheloai
                res += " , "
    res = res[:-2]
    return res

def getNewChap(id):
    mylist = getAllChap(id)
    mylist = sorted(mylist, key=lambda x: x.thoigian, reverse=True)
    res = []
    index = 0
    for i in mylist:
        if (index < 5):
            res.append(i)
        index += 1;
    return res

def getAllChap(id):
    mylist = Chaptruyen.objects.all()
    res = []
    for i in mylist:
        if i.IDtruyen.pk == id:
            res.append(i)
    return res

def getFirstChap(id):
    temp = getAllChap(id)
    res = 0
    check = False
    for i in temp:
        if i.IDtruyen.pk == id and check == False:
            res = i.id
            check = True
    return res
def getNumberChap(id):
    temp = getAllChap(id)
    res = 0
    for i in temp:
        if i.IDtruyen.pk == id:
            res +=1
    return res

def getSameType(id):
    myTruyen = Truyen.objects.get(IDtruyen=id)
    listTheLoai = Checktheloai.objects.filter(IDtruyen=myTruyen.IDtruyen)
    temp = []
    for item in listTheLoai:
        temp.append(item.IDtheloai.pk)
    tempTruyen = []
    fullTheLoai = Checktheloai.objects.all()
    for theloai in fullTheLoai:
        for p in temp:
            if theloai.IDtheloai.pk == p:
                tempTruyen.append(theloai.IDtruyen.pk)
    fullTruyen = Truyen.objects.all()
    res = []
    index = 0
    for truyen in fullTruyen:
        for a in tempTruyen:
            if truyen.IDtruyen == a and truyen.IDtruyen != id:
                check = False
                for b in res:
                    if b.IDtruyen == truyen.IDtruyen:
                        check = True
                if check == False and index < 5:
                    res.append(truyen)
                    index += 1
    return res