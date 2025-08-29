from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import logout
from .form import *
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def activities(request):
  return render(request, 'activities.html')

@login_required
def challenges(request):
  return render(request, 'challenges.html')

@login_required
def analytics(request):
  return render(request, 'analytics.html')

@login_required
def dashboard(request):
  return render(request, 'dashboard.html')

def is_admin(user):
    return user.is_staff or user.is_superuser
   
@user_passes_test(is_admin, login_url='login_user')
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

@login_required
def profile(request):
    return render(request, 'auth/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save()
          auth_login(request, user)
          messages.success(request, 'Signed up successfully!')
          return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})
  

@require_http_methods(["GET", "POST"])
def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me', False)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(1209600)  # 2 weeks
                messages.success(request, 'Login successful!')
              
                if user.is_staff:
                    messages.info(request, f'Welcome back, Admin {user.username}!')
                    return redirect('admin_dashboard')
                else:
                    messages.info(request, f'Welcome back, {user.username}!')
                    return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'auth/login.html', {'form': form})

@require_http_methods(["POST"])
def logout_user(request):
  logout(request)
  messages.success(request, 'Logout was successful!')
  return redirect('login')


class WorkoutList(generics.ListCreateAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user)

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user)
      
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            messages.success(request, 'Workout created successfully!')
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutSessionForm()
    return render(request, 'workouts/workout_form.html', {'form': form})