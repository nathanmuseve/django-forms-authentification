from django.shortcuts import render
from . import views
from django.urls import path

urlpatterns = [
  path('', views.home, name='home'),
  path('register/', views.register_view, name='register'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('protected/', views.ProtectedView.as_view(), name='protected'),
]
