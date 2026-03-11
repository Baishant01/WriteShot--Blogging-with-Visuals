from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProfileEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            messages.success(request, "User registration successful!")
            user = form.save()

            Profile.objects.create(
                user=user, profile_pic=request.FILES.get("profile_pic")
            )
            return redirect("post_list")
        else:
            messages.error(request, "Error submitting form...")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    next_url = request.GET.get("next") or request.POST.get("next")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")

            if next_url:
                return redirect(next_url)
            return redirect("post_list")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html", {"next": next_url})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {"profile": profile}
    return render(request, "accounts/profile_view.html", context)


@login_required
def profile_edit_view(request):

    profile = get_object_or_404(Profile, user=request.user)
    old_profile_pic = profile.profile_pic
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            if "profile_pic" in request.FILES and old_profile_pic:
                old_profile_pic.delete(save=False)
            messages.success(request, "Profile updated successfully!")
            return redirect("profile_view")
        else:
            messages.error(request, "Profile submission error...")

    else:
        form = ProfileEditForm(instance=profile)
    context = {"form": form, "profile": profile}
    return render(request, "accounts/profile_edit.html", context)
