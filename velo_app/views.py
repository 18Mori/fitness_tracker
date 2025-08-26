from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from .form import UserLoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import generics
from .models import *
from .serializers import *

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dashboard(request):
  return render(request, 'dashboard.html')

def is_admin(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def profile(request):
    return render(request, 'auth/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save()
          auth_login(request, user)
          messages.success(request, 'Signed up successfully!')
          return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})
  
@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
      
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            remember_me = request.POST.get('remember_me', False)
            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            if remember_me: 
                request.session.set_expiry(1209600)  # 2 weeks
                return redirect('home')
                
            elif user.is_staff:
                auth_login(request, user)
                messages.success(request, 'Welcome back, Admin {}'.format(user.username))
                if remember_me: 
                    request.session.set_expiry(1209600)  # 2 weeks
                    return redirect('admin_dashboard')
            return redirect('admin_dashboard')
            
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})

@require_POST
@login_required
def logout_user(request):
  logout(request)
  messages.success(request, 'Logout was successful!')
  return redirect('home')

class WorkoutList(generics.ListCreateAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer