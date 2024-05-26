from django.shortcuts import render, get_object_or_404
from game.game_state import GameState
from game.forms import ClueForm
from home.models import *
from django.shortcuts import redirect


# Create your views here.
def teamSelect(request):
    return render(request, 'game/teamSelect.html')

def victory(request):
    context = {
        'teamWon' : 'Blue'
    }
    return render(request, 'game/victory.html', context)


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

    # TEAM DOHVATITI IZ COOKIES
    team = 'blue'
    myTurn = False
    if (GameState.turn == 2) and (team == 'blue'):
        myTurn = True
    elif (GameState.turn == 4) and (team == 'red'):
        myTurn = True

    if request.method == "POST":
        form = ClueForm(request.POST)
        if form.is_valid():
            clue = form.cleaned_data['clue']
            clue_num = form.cleaned_data['clue_num']

            GameState.clue = clue
            GameState.clue_num = clue_num

            # Dodati u bazu za asoc -> SAMO AKO JE KORISNIK ULOGOVAN
            if request.user != None:
                pass

            GameState.turn = 3

            return redirect('leader')
    else:
        form = ClueForm()
    context = {
        'gamestate': GameState,
        'form': form,
        'myTurn':myTurn
    }
    return render(request, 'game/leader.html', context)


def reroll(request):
    if not GameState.is_game_init:
        GameState.init_words()

    # Logika koji igrac igra za default neka bude red
    specific_player_words = {key: value for key, value in GameState.game_words.items() if value[0] == "red"}

    context = {
        'specific_player_words': specific_player_words,
        'gamestate': GameState
    }

    return render(request, 'game/reroll.html', context)
