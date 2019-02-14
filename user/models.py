from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
# Create your models here.

cloudinary.config( 
  secure=True,
  cloud_name = "prakhargurunani", 
  api_key = "252412724742197", 
  api_secret = "LA9lwVhzVMlXOKGSOfDTU9QAUjQ" 
)

class UserDetail(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    portfolio_site = models.URLField(blank=True)
    profile_picture = CloudinaryField('image', null=True, blank=True)
    def __str__(self):
        return self.user.username

class Post(models.Model): 

    author = models.OneToOneField(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50) 
    slug = models.SlugField(max_length=50, help_text="Slug will be generated automatically from the title of the post")
    post_image = CloudinaryField('image', blank=True, null=True)
    content = RichTextField()  
    published_date = models.DateTimeField(default=timezone.now) 

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title 