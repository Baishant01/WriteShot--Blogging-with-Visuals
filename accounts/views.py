from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Profile
# Create your views here.

def register_view (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        
        if form.is_valid():
            messages.success(request, 'User registration successful!')
            user = form.save()
            
            Profile.objects.create(
                user = user,
                profile_pic = request.FILES.get('profile_pic')
                
            ) 
            return redirect('post_list')
        else:
            messages.error(request, "Error submitting form...")
    else:
        form = RegisterForm()
    return render (request, 'accounts/register.html', {'form':form})
    
def login_view (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect ('post_list')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render (request, 'accounts/login.html')

def logout_view (request):
    logout(request)
    return redirect ('login')
