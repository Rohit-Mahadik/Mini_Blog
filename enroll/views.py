from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Post
from django.contrib.auth.models import User,Group
# Create your views here.

#Home

def home(request):
    posts=Post.objects.all()
    return render(request,'enroll/home.html',{'posts':posts,'name':request.user})


def about(request):
    return render(request,'enroll/about.html')

def contact(request):
    return render(request,'enroll/contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        return render(request,'enroll/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')



def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                upass=form.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
        return render(request,'enroll/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registration Successfully')
            user=form.save()
            group=Group.objects.get(name="Students")
            user.groups.add(group)
    else:
        form=SignupForm()
    return render(request,'enroll/signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=PostForm(request.POST)
            if form.is_valid():
                form.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request,'enroll/add_post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                messages.success(request,"Updated Successfully")
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,'enroll/update_post.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
