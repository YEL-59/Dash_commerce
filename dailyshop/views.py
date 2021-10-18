from django.shortcuts import render,redirect
from .forms import CreateUserFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):

    return render(request,'index.html')


def register_page_login(request, ):

    form = CreateUserFrom()
    if request.method == "POST":
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'User create successfull ' + username)
            return redirect('register')
    context = {"forms": form}
    return render(request,'account.html',context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user.id)

            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login.html')