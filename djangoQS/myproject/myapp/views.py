from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def myview(request):
    return render(request, "index.html")

def UserRegister(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')        
    return render(request, "register.html")

def UserLogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/profile")
        else:
            return HttpResponse("User not Found")
        alert = True
        return render(request, 'login.html', {'alert':alert})            
    return render(request, "login.html")

def myprofile(request):
    if request.method=="POST":
        user = request.user    
        profile = Profile(user=user)
        profile.save()
        form = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "profile.html",{'obj':obj})
    else:
        form=ProfileForm()
    return render(request, "profile.html", {'form':form})

