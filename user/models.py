from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

# Create your models here.

class UserDetail(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture',blank=True, null=True, default="static/images/logo.png")
    def __str__(self):
        return self.user.username

class Post(models.Model): 

    author = models.ForeignKey('UserDetail', on_delete=models.CASCADE) 
    title = models.CharField(max_length=50) 
    text = models.TextField() 
    created_date = models.DateTimeField(default=timezone.now) 
    published_date = models.DateTimeField(blank=True, null=True) 

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title 