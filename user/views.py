from django.shortcuts import render
from user.forms import UserForm, UserDetailForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from django.utils import timezone
from django.contrib.auth.models import User
from .models import UserDetail

def index(request):
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    context = dict( backend_form = UserDetailForm())
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_detail_form = UserDetailForm(request.POST, request.FILES)
        context['posted'] = user_detail_form.instance
        if user_form.is_valid() and user_detail_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_detail_form.save(commit=False)
            profile.user = user
            if 'profile_picture' in request.FILES:
                print('found profile picture')
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, user_detail_form.errors)
    else:
        user_form = UserForm()
        user_detail_form = UserDetailForm()
    return render(request,'user/registration.html',
                          {'user_form':user_form,
                           'user_detail_form':user_detail_form,
                           'registered':registered}, context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not found !")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user/login.html', {})

@login_required
def write(request):
    written = False
    post_context_detail = dict( post_backend_form = PostForm())
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        post_context_detail['posted'] = post_form.instance
        if post_form.is_valid():
            my_post = post_form.save(commit=False)
            my_post.author = request.user
            my_post.published_date = timezone.now()
            if 'post_image' in request.FILES:
                print('found post image')
                my_post.post_image = request.FILES['post_image']
            my_post.save()
            written = True
        else:
            print(post_form.errors)
    else:
        post_form = PostForm()
    return render(request,'user/write.html',
                          {'post_form':post_form, 'written':written}, post_context_detail)

def user_profile(request, username):
    user_username = User.objects.get(username=username)
    user_image = user_username.userdetail.profile_picture
    user_bio = user_username.userdetail.bio
    user_portfolio_site = user_username.userdetail.portfolio_site
    return render(request, 'user/profile.html', {'user_username':user_username,
                                                 'user_image':user_image,
                                                 'user_bio':user_bio,
                                                 'user_portfolio_site':user_portfolio_site})