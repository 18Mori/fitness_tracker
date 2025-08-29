from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('activities/', views.activities, name='activities'),
    path('challenges/', views.challenges, name='challenges'),
    path('analytics/', views.analytics, name='analytics'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('workouts/', views.WorkoutList.as_view(), name='workout_list'),
    path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name='workout_detail'),
]