from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib import messages

# Create your views here.

def post_list (request):
    posts = Post.objects.all().order_by('-created_at')
    return render (request, 'blog_app/post_list.html', {'posts':posts})

def post_details (request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post:
        return render (request, 'blog_app/post_detail.html', {'post':post})
    else:
        messages.error(request, 'Error while fetching details...')
    return render (request, 'blog_app/post_list.html')

def post_create (request):
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

def post_delete (request, pk):
    post_obj = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # To delete images from media folder if available
        if post_obj.image:
            post_obj.image.delete()
            
        # To delete selected post object from database
        post_obj.delete()
        messages.success(request, 'Post deletion successful!')
        return render ('post_list')
    return render (request, 'blog_app/post_confirm_delete.html', {'post_obj':post_obj})
        