from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from Data.formResgister import CreateUserForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Home Page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tạo tài khoản thành công')
                return redirect('login')

        context = {'form' : form}
        return render(request, 'Auth/registerPage.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home Page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
    #Redirect to homepage using homepage's name
                return redirect('Home Page')
            else:
                messages.info(request, 'Tên tài khoản mật khẩu không đúng !!!')
        context = {}
        return render(request, 'Auth/loginPage.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')