from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(is_private=False).order_by("-created_at")
    paginator = Paginator(posts, 9)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)
    return render(request, "blog_app/post_list.html", {"page_obj": page_obj})


def post_details(request, pk, title):
    post = get_object_or_404(Post, pk=pk, title=title)
    if post.is_private and post.author != request.user:
        return redirect("post_list")
    return render(request, "blog_app/post_detail.html", {"post": post})


@login_required
def my_posts_view(request):
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts, 9)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)
    return render(request, "blog_app/my_posts.html", {"page_obj": page_obj})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Successfully submitted form!")
            return redirect("post_list")
        else:
            messages.error(request, "Error while submitting form...")
    else:
        form = PostForm()
    return render(request, "blog_app/post_form.html", {"form": form})


@login_required
def post_edit(request, pk, title):
    post_obj = get_object_or_404(Post, pk=pk, title=title, author=request.user)
    old_image = post_obj.image
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post_obj)
        if form.is_valid():
            updated_post = form.save()
            if "image" in request.FILES:
                if old_image and old_image != updated_post.image:
                    old_image.delete(save=False)

            messages.success(request, "Post updated successfully!")
            return redirect("post_details", pk=post_obj.pk, title=post_obj.title)
        else:
            messages.error(request, "Error while updating post...")
    else:
        form = PostForm(instance=post_obj)

    return render(request, "blog_app/post_form.html", {"form": form, "post": post_obj})


@login_required
def post_delete(request, pk, title):
    post_obj = get_object_or_404(Post, pk=pk, title=title, author=request.user)
    if request.method == "POST":
        # To delete images from media folder if available
        if post_obj.image:
            post_obj.image.delete(save=False)

        # To delete selected post object from database
        post_obj.delete()
        messages.success(request, "Post deletion successful!")
        return redirect("post_list")
    return render(request, "blog_app/post_confirm_delete.html", {"post_obj": post_obj})
