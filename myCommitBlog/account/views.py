from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request = request, username=username,password=password)
            if user is not None:
                login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect('home')    
    else:
        form = RegisterForm()
        return render(request,'signup.html',{'form':form})

@login_required
def profile(request, id):
    profile = CustomUser.objects.get(id=id)
    return render(request, 'profile.html', {'user':profile})

@login_required
def update_profile(request, id):
    if request.method == "GET":
        editProfile = CustomUser.objects.get(id=id)
        return render(request, 'edit_profile.html', {'user':editProfile})
    else:
        editProfile = CustomUser.objects.get(id=id)
        editProfile.username = request.POST.get('username')
        editProfile.shortDescription = request.POST.get('shortDescription')
        editProfile.fullDescription = request.POST.get('fullDescription')
        editProfile.github = request.POST.get('github')
        editProfile.token = request.POST.get('token')
        editProfile.save()
        return redirect('profile', editProfile.id)


