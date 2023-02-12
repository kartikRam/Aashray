from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import circular , profile_phil

@login_required(login_url='login')
def index(request):
    return render(request,'ashrayapp/index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        typeu = request.POST.get('type')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            if typeu == 'Philanthroper':
                login(request,user)
                return redirect('index')
            elif typeu == 'NGO':
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
    blogs = circular.objects.all()
    context = {'blogs':blogs}
    return render(request,'ashrayapp/news.html',context)

@login_required(login_url='login')
def chat(request):
    return render(request,'ashrayapp/chat.html')

# @login_required(login_url='login')
# def profile_phi(request):
#     details = profile_phil.objects.all()
#     context = {'details':details}
#     return render(request,'ashrayapp/prophi.html',context)

def propli_up(request):
    return render(request,'ashrayapp/prophi_up.html')

@login_required(login_url='login')
def pro_ngo(request):
    return render(request,'ashrayapp/pro_ngo.html')

@login_required(login_url='login')
def add_post(request):
    return render(request,'ashrayapp/add_post.html')

def explore(request):
    return render(request,'ashrayapp/explore.html')