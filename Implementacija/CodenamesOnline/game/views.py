from django.shortcuts import render, get_object_or_404
from game.game_state import GameState
from game.forms import ClueForm
from home.models import Asocijacija
from django.shortcuts import redirect

# Create your views here.
def teamSelect(request):
    return render(request, 'game/teamSelect.html')

def guesser(request):
    if not GameState.is_game_init:
        GameState.init_words()

    context = {
        'gamestate': GameState
    }
    return render(request, 'game/guesser.html', context)

def leader(request):
    if not GameState.is_game_init:
        GameState.init_words()

    if request.method == "POST":
        form = ClueForm(request.POST)
        if form.is_valid():
            clue = form.cleaned_data['clue']
            clue_num = form.cleaned_data['clue_num']

            GameState.clue = clue
            GameState.clue_num = clue_num

            # Dodati u bazu za asoc

            return redirect('guesser')
    else:
        form = ClueForm()
    context = {
        'gamestate': GameState,
        'form': form
    }
    return render(request, 'game/leader.html', context)

def reroll(request):
    return render(request, 'game/reroll.html')




