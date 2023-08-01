from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


# Create your views here.


def home(request):
    context = {}

    if request.POST:
        query = request.POST.get('query')
        all_blogs = blog.objects.filter(title__contains=query, is_verified=True).order_by('-date')
    else:
        all_blogs = blog.objects.filter(is_verified=True).order_by('-date')

    if request.user.is_authenticated:
        context['bloger'] = user_profile.objects.filter(user=request.user).first()

    context['all_blogs'] = all_blogs
    context['all_categories'] = blog_category.objects.all()
    return render(request, 'home.html', context)


def filter_by_category(request, id):
    context = {}
    all_blogs = blog.objects.filter(category__id=id)
    if request.user.is_authenticated:
        context['bloger'] = user_profile.objects.filter(user=request.user).first()

    context['all_blogs'] = all_blogs
    context['all_categories'] = blog_category.objects.all()
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save user information
            user = form.save()
            # Save candidate information
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            user_profile.objects.create(user=user, name=name, email=email, phone=phone)
            messages.success(request, "You account created Successfully ")
            return redirect('user-login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'Please Enter valid credentials')
            return redirect('user-login')
    else:
        return render(request, 'login.html')


def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def blog_view(request, pk):
    context = {}
    get_blog = blog.objects.filter(id=pk).first()
    allcomments = get_blog.blog_comments.filter(status=True)
    comment_form = NewCommentForm()

    if request.user.is_authenticated:
        context['bloger'] = user_profile.objects.filter(user=request.user).first()

    context['post'] = get_blog
    context['allcomments'] = allcomments
    context['comment_form'] = comment_form

    return render(request, 'blog_view.html', context)


def add_blog(request):
    form = AddBlog()
    get_user = user_profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = AddBlog(request.POST)
        if form.is_valid():
            fr = form.save(commit=False)
            fr.user = get_user
            fr.save()
            messages.success(request, 'Blog added Successfully')
            return redirect('home')
    return render(request, 'blog.html',
                  {'form': form, 'bloger': user_profile.objects.filter(user=request.user).first()})


def addcomment(request):
    get_student = user_profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            id = request.POST.get('nodeid')
            print(id)
            c = Comment.objects.get(id=id)
            c.delete()
            return JsonResponse({'remove': id})
        else:
            comment_form = NewCommentForm(request.POST)
            print(comment_form)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                result = comment_form.cleaned_data.get('content')
                user = request.user.username
                user_comment.user = get_student
                user_comment.save()
                return JsonResponse({'result': result, 'user': user})


def update_blog(request, pk):
    blog_obj = blog.objects.get(pk=pk)
    form = AddBlog(instance=blog_obj)
    if request.method == 'POST':
        form = AddBlog(request.POST, instance=blog_obj)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'blog.html',
                  {'form': form, 'bloger': user_profile.objects.filter(user=request.user).first()})


def delete_blog(request, pk):
    blog_obj = blog.objects.get(pk=pk)
    blog_obj.delete()
    messages.success(request, 'deleted successfully')
    return redirect('profile')


def profile(request):
    get_user = user_profile.objects.get(user=request.user)
    all_blogs = blog.objects.filter(user=get_user)
    return render(request, 'profile.html', {'all_blogs': all_blogs, 'bloger': get_user})


class UserProfileUpdateView(UpdateView):
    model = user_profile
    form_class = UserProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')

# For Blog Application

# Features:
# • User Registration and Login with secure password storage.
# • Create, Edit, and Delete blog posts with a user-friendly editor and image uploading capabilities.
# * Categorize blog posts and provide a search functionality.
# Allow users to comment on blog posts with moderation options.
# • Social media sharing options for blog posts.
# •Email notifications for user interactions (e.g., new comments, replies).
# • User profile management with the ability to update personal information and profile picture.
# • Admin panel for blog management and moderation.
