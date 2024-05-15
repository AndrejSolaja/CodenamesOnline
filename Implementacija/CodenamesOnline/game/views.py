from django.shortcuts import render, get_object_or_404
from game.game_functions import GameState

# Create your views here.
def teamSelect(request):
    return render(request, 'game/teamSelect.html')

def guesser(request):
    if not GameState.is_game_init:
        GameState.init_words()

    context = {
        'words': GameState.game_words,
    }
    return render(request, 'game/guesser.html', context)

def leader(request):
    print("LEADER", GameState.is_game_init)
    if not GameState.is_game_init:
        GameState.init_words()

    context = {
        'words': GameState.game_words,
    }
    return render(request, 'game/leader.html', context)

def reroll(request):
    return render(request, 'game/reroll.html')