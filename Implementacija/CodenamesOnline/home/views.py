from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def login_req(request):
    return render(request, 'home/login.html')

def newset(request):
    return render(request, 'home/newSet.html')

def profile(request):
    context = {
        'image' : 0
    }
    return render(request, 'home/profile.html', context)

def recovery(request):
    return render(request, 'home/recovery.html')

def register(request):
    return render(request, 'home/register.html')

def rules(request):
    return render(request, 'home/rules.html')