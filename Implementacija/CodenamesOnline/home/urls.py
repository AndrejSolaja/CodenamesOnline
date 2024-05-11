from django.contrib import admin
from django.urls import path, include
from home.views import home, login_req, newset, profile, recovery,register, rules

urlpatterns = [
    path('', home, name='home'),
    path('login', login_req, name='login'),
    path('newset', newset, name='newset'),
    path('profile', profile, name='profile'),
    path('recovery', recovery, name='recovery'),
    path('register', register, name='register'),
    path('rules', rules, name='rules'),
]