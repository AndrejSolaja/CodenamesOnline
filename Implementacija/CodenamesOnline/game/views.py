from django.shortcuts import render

# Create your views here.
def teamSelect(request):
    return render(request, 'game/teamSelect.html')

def guesser(request):
    return render(request, 'game/guesser.html')

def leader(request):
    return render(request, 'game/leader.html')

def reroll(request):
    return render(request, 'game/reroll.html')