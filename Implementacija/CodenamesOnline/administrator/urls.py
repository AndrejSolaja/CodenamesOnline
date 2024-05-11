from django.urls import path
from administrator.views import adminPage

urlpatterns = [
    path('', adminPage, name='adminPage'),
]