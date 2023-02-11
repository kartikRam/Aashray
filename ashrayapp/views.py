from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request,'ashrayapp/index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect !!')
            
    return render(request,'ashrayapp/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') 
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
    context = { 'form': form}
    return render(request,'ashrayapp/signup.html',context)

@login_required(login_url='login')
def profile(request):
    return render(request,'ashrayapp/profile.html')

@login_required(login_url='login')
def news(request):
    return render(request,'ashrayapp/news.html')

@login_required(login_url='login')
def chat(request):
    return render(request,'ashrayapp/chat.html')