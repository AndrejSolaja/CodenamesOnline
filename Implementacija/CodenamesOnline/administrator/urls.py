from django.urls import path
from administrator.views import adminPage, adminSetEditor

urlpatterns = [
    path('', adminPage, name='adminPage'),
    path('<int:set_id>', adminSetEditor, name='adminSetEditor'),
]