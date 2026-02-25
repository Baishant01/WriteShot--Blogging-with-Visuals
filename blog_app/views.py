from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib import messages

# Create your views here.

def post_list (request):
    posts = Post.objects.all().order_by('-created_at')
    return render (request, 'blog_app/post_list.html', {'posts':posts})

def post_details (request):
    return render (request, 'blog_app/post_detail.html')

def post_form (request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submitted form!')
            return redirect ('post_list')
        else:
            messages.error(request, 'Error while submitting form...')
    else:
        form = PostForm()
    return render (request, 'blog_app/post_form.html', {'form':form})