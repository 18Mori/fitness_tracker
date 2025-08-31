from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('activities/', views.activities, name='activities'),
    path('challenges/', views.challenges, name='challenges'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('account/<int:pk>/', views.account_logout, name='account_logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('activities/', views.activities, name='activity_create'),
    path('activities/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('activities/<int:pk>/edit/', views.activity_edit, name='activity_edit'),
    path('activities/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
]