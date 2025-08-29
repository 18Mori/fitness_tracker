from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember_me = forms.BooleanField(required=False, initial=False)

class UserForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True)

     
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'age']

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['title', 'description', 'type', 'target', 'start_date', 'end_date']
        
class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description', 'target_date']
        
class ActivityForm(forms.ModelForm):
    class Meta:
        model = ActivityTrackerLog
        fields = ['activity_type', 'duration', 'date', 'calories_burned']

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['workout_type', 'duration', 'calories_burned']