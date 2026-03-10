from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Like
from blog_app.models import Post
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# add_comment_view


@login_required
def toggle_like_view(request, id):
    post = get_object_or_404(Post, id=id)

    existing_like = post.likes.filter(user=request.user).first()

    if existing_like:
        existing_like.delete()
    else:
        post.likes.create(user=request.user)
    return redirect("post_details", pk=post.pk, title=post.title)


@login_required
def add_comment_view(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_form = form.save(commit=False)

            comment_form.post = post
            comment_form.user = request.user

            comment_form.save()

            messages.success(request, "Comment added successfully!")
        else:
            messages.error(request, "Error while submitting form")

    return redirect("post_details", pk=post.pk, title=post.title)
