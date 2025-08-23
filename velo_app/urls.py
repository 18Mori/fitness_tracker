from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('workouts/', views.WorkoutList.as_view(), name='workout_list'),
    path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name='workout_detail'),
]