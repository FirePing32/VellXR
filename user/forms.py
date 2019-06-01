from django import forms
from user.models import UserDetail
from user.models import Post
from django.contrib.auth.models import User
from django.forms import widgets
from ckeditor.widgets import CKEditorWidget

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
    bio = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    portfolio_site = forms.CharField(required=False, widget=forms.URLInput(attrs={'class':'form-control text-center'}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control text-center custom-file custom-file-input btn btn-default btn-file input-group-text', 'id':'inputGroupFile01', 'aria-describedby':'inputGroupFileAddon01', 'style':'text-align: center; vertical-align: center; width: 100%; height: 100%;'}))

    class Meta():
        model = UserDetail
        fields = ('bio', 'portfolio_site', 'profile_picture')

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    post_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control text-center custom-file custom-file-input btn btn-default btn-file input-group-text', 'id':'inputGroupFile01', 'aria-describedby':'inputGroupFileAddon01', 'style':'text-align: center; vertical-align: center; width: 100%; height: 100%;'}))
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))

    class Meta():
        model = Post
        fields = ('title', 'post_image', 'content')
        widgets = {
            'my_field': CKEditorWidget(attrs={
                'class': 'my-ckeditor-class',
                'id': 'my-ckeditor-id'
            })
        }