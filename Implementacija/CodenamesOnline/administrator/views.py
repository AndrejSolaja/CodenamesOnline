from django.shortcuts import render

# Create your views here.

def adminPage(request):
    return render(request, 'administrator/adminPage.html')