"""vellxr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from user import views
from . import settings
import ckeditor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor.urls')),
    url(r'^$',views.index, name='index'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.user_login, name='login'),
    url(r'^about/$', views.about, name='about'),
    url(r'^write/$', views.write, name='write'),
    url(r'^profile/(?P<username>[-\w.]+)/$', views.user_profile, name='profile'),
    url(r'^profile/(?P<username>[-\w.]+)/posts/$', views.profile_posts, name='profile_posts'),
    url(r'^profile/(?P<username>[-\w.]+)/posts/(?P<slug>[-\w.]+)/$', views.profile_posts_detail, name='profile_posts_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
