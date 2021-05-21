from django.shortcuts import render
from Data.models import Truyen
from Data.models import Chaptruyen


def home(request):
    context = {
        "listTruyen":getThisView(),
        "topView":getTopview(),
        "newView":getNewView(),
        "loveView":getLoveView(),
        "newChap":getNewChap()
    }
    return render(request, "Home/index.html",context)

def getNewView():
    mylist = Truyen.objects.all()
    mylist = reversed(mylist)
    res = []
    index = 0
    for i in mylist:
        if(index<10):
            res.append(i)
        index += 1;
    return res

def getTopview():
    mylist = Truyen.objects.all()
    tempList = sorted(mylist, key=lambda x: x.luotxem, reverse=True)
    topView = []
    index = 0;
    for i in tempList:
        if(index<10):
            topView.append(i)
        index += 1;
    return topView

def getThisView():
    mylist = Truyen.objects.all()
    mylist = sorted(mylist, key=lambda x: x.luotxem, reverse=True)
    res = []
    index = 0
    for i in mylist:
        if (index < 20):
            res.append(i)
        index += 1;
    return res

def getLoveView():
    mylist = Truyen.objects.all()
    mylist = sorted(mylist, key=lambda x: x.yeuthich, reverse=True)
    res = []
    index = 0
    for i in mylist:
        if (index < 20):
            res.append(i)
        index += 1;
    return res
def getNewChap():
    mylist = Chaptruyen.objects.all()
    mylist = sorted(mylist, key=lambda x: x.thoigian, reverse=True)
    res = []
    index = 0
    for i in mylist:
        if (index < 10):
            res.append(i)
        index += 1;
    return res