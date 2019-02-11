from django import forms
from user.models import UserDetail
from django.contrib.auth.models import User
from django.forms import widgets

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    username = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control text-center', 'type':'username', 'id':'exampleInputEmail1'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control text-center', 'type':'password', 'id':'exampleInputPassword1'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UserDetailForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    portfolio_site = forms.CharField(widget=forms.URLInput(attrs={'class':'form-control text-center'}))
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control text-center input-group input-group-prepend btn input-group-text', 'id':'inputGroupFileAddon01', 'style':'text-align: center; vertical-align: center; width: 100%; height: 100%;'}), upload_to='profile_picture', null=True, blank=True)

    class Meta():
        model = UserDetail
        fields = ('bio', 'portfolio_site', 'profile_picture')
