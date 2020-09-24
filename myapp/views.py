from django.shortcuts import render,redirect
from myapp.forms import RegistrationForm,PasswordResetForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"myapp/home.html")

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
        else:
            return render(request,"myapp/register.html",{'form':form})
    form=RegistrationForm()
    return render(request,"myapp/register.html",{'form':form})

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        pwd=request.POST.get('pwd')
        user=authenticate(request,username=username,password=pwd)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('myapp:home')
        else:
            return redirect('myapp:home')
    return render(request,'myapp/user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('myapp:home')

@login_required(login_url='/login/')
def profile(request):
    return render(request,"myapp/profile.html")

@login_required(login_url='/login/')
def reset_password(request):
    form=PasswordResetForm()
    if request.method=="POST":
        form=PasswordResetForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            request.user.set_password(password)
            request.user.save()
        else:
            return render(request,'myapp/forgot_passsword.html',{'form':form})
    return render(request,'myapp/forgot_password.html',{'form':form})