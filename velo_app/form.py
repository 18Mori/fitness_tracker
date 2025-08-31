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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'current_weight', 'target_weight', 'age', 'fitness_level']
        widgets = {
            'height': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'current_weight': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'target_weight': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'age': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'fitness_level': forms.Select(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['title', 'description', 'type', 'target', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'type': forms.Select(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'target': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'start_date': forms.DateInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500', 'type': 'date'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = ActivityTrackerLog
        fields = ['activity_type', 'duration', 'date', 'calories_burned']
        widgets = {
            'activity_type': forms.Select(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'date': forms.DateInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500', 'type': 'date'}),
            'duration': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'steps': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'calories_burned': forms.NumberInput(attrs={'class': 'w-full p-2.5 rounded-md bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }