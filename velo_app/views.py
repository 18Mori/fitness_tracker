from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            messages.success(request, 'Activity logged successfully!')
            return redirect('activities')
    else:
        form = ActivityForm()
    user_activities = ActivityTrackerLog.objects.filter(user=request.user)
    return render(request, 'activities.html', {'form': form, 'user_activities': user_activities})

def increment_view_count(activity):
    activity.view_count += 1
    activity.save()

@login_required
def activity_detail(request, pk):
    activity = get_object_or_404(ActivityTrackerLog, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity updated successfully!')
            return redirect('activities')
    else:
        form = ActivityForm(instance=activity)
    
    return render(request, 'activity_detail.html', {'form': form, 'activity': activity})

@login_required
def activity_delete(request, pk):
    activity = get_object_or_404(ActivityTrackerLog, pk=pk, user=request.user)
    if request.method == 'POST':
        activity.delete()
        messages.success(request, 'Activity deleted successfully!')
        return redirect('activities')
    return redirect('activities')

def activity_edit(request, pk):
    activity = get_object_or_404(ActivityTrackerLog, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity updated successfully!')
            return redirect('activities')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activity_detail.html', {'form': form, 'activity': activity})

@login_required
def challenges(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.user = request.user
            challenge.save()
            messages.success(request, 'Challenge created successfully!')
            return redirect('challenges')
    else:
        form = ChallengeForm()
    user_challenges = Challenge.objects.filter(user=request.user)
    return render(request, 'challenges.html', {'form': form, 'user_challenges': user_challenges})

@login_required
def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            form.save()
            messages.success(request, 'Challenge updated successfully!')
            return redirect('challenges')
    else:
        form = ChallengeForm(instance=challenge)

    return render(request, 'challenge_detail.html', {'form': form, 'challenge': challenge})

@login_required
def analytics(request):
    user_activities = ActivityTrackerLog.objects.filter(user=request.user)
    return render(request, 'analytics.html', {'user_activities': user_activities})

@login_required
def dashboard(request):
    user_activities = ActivityTrackerLog.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'user_activities': user_activities})

def is_admin(user):
    return user.is_staff or user.is_superuser
   
@user_passes_test(is_admin, login_url='login_user')
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

@login_required
def profile_detail(request, pk):
    user_profile = get_object_or_404(User, pk=pk)
    return render(request, 'profile_detail.html', {'user_profile': user_profile})

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