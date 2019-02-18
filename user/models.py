from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import datetime

User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True

cloudinary.config( 
  secure=True,
  cloud_name = "prakhargurunani", 
  api_key = "252412724742197", 
  api_secret = "LA9lwVhzVMlXOKGSOfDTU9QAUjQ" 
)

class UserDetail(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, blank=True)
    portfolio_site = models.URLField(blank=True)
    profile_picture = CloudinaryField('image', null=True, blank=True, default="logo.png")
    def __str__(self):
        return self.user.username

class Post(models.Model): 

    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=50) 
    post_image = CloudinaryField('image', blank=True, null=True, default="logo.png")
    content = RichTextField()  
    published_date = models.DateTimeField(default=timezone.now) 

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title 

    def save(self):
        super(Post, self).save()
        date = datetime.date.today()
        self.slug = '%s-%i%i%i%i' % (
            slugify(self.title), datetime.time, date.day, date.month, date.year
        )
        super(Post, self).save()
