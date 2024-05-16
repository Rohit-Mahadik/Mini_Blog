from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post

class SignupForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control mt-3"}))
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':"form-control mt-3"}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}
        widgets={'username':forms.TextInput(attrs={'class':"form-control mt-3"}),'first_name':forms.TextInput(attrs={'class':"form-control mt-3"}),'last_name':forms.TextInput(attrs={'class':"form-control mt-3"}),'email':forms.EmailInput(attrs={'class':"form-control mt-3"}),}

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={"autofocus":True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"current-password",'class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['tittle',"desc"]
        labels={'tittle':'Title','desc':"Description"}
        widgets={"tittle":forms.TextInput(attrs={'class':'form-control'}),
        "desc":forms.Textarea(attrs={'class':'form-control'})}