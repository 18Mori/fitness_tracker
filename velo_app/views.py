from django.shortcuts import render, redirect, get_object_or_404
from .form import UserRegistrationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save()
          auth_login(request, user)
          return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
  
@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
      
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      remember_me = request.POST.get('remember_me', False)
      user = authenticate(request, username=username, password=password)

      if user is not None:
          auth_login(request, user)
          if remember_me:
              request.session.set_expiry(1209600)  # 2 weeks
          return redirect('home')
      else:
          messages.error(request, 'Invalid username or password.')
    return render(request, 'auth/login.html')

@require_POST
@login_required
def logout_user(request):
  logout(request)
  return redirect('home')