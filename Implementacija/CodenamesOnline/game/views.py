from django.shortcuts import render, get_object_or_404
from game.game_state import GameState
from game.forms import ClueForm, TeamSelect
from home.models import *
from django.shortcuts import redirect

from django.http import HttpResponse
import json

import uuid

def generateId(request):

    if request.user.is_authenticated:
        return request.user.id

    return uuid.uuid4().hex

def getId(request):
    if request.user.is_authenticated:
        return request.user.id

    if 'playerIdentifier' in request.COOKIES.keys():
        return uuid.UUID(request.COOKIES['playerIdentifier']).hex

    return None

def players(request):        
    return HttpResponse(
            json.dumps([GameState.redLeaderId != None, GameState.redGuesserId != None, GameState.blueLeaderId != None, GameState.blueGuesserId != None]),
            content_type="application/json")

# Create your views here.
def teamSelect(request):

    if not GameState.is_game_init:
        GameState.init_words()

    playerId = getId(request)

    if playerId != None:
        if GameState.redLeaderId == playerId or GameState.blueLeaderId == playerId:
            return redirect("leader")
        elif GameState.redGuesserId == playerId or GameState.blueGuesserId == playerId:
            return redirect("guesser")

    if request.method == "POST":

        form = TeamSelect(request.POST)

        if(form.is_valid()):
            playerId = form.cleaned_data['playerId']

            generatedId = generateId(request)

            redirectLocation = ""

            if playerId == 0:
                if GameState.redLeaderId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.redLeaderId = generatedId
                redirectLocation = "leader"
            elif playerId == 1:
                if GameState.redGuesserId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.redGuesserId = generatedId
                redirectLocation = "guesser"
            elif playerId == 2:
                if GameState.blueLeaderId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.blueLeaderId = generatedId
                redirectLocation = "leader"
            else:
                if GameState.blueGuesserId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.blueGuesserId = generatedId
                redirectLocation = "guesser"            
        
            response = redirect(redirectLocation)

            if not request.user.is_authenticated:
                response.set_cookie("playerIdentifier", generatedId)

            return response

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
