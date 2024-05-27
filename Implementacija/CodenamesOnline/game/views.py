from django.shortcuts import render, get_object_or_404
from game.game_state import GameState
from game.forms import ClueForm, TeamSelect
from home.models import *
from django.shortcuts import redirect

from django.http import HttpResponse, HttpResponseForbidden
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

    # odredjivanje tima na osnovu requesta
    if request.user.id == None:
        if GameState.blueGuesserId == request.COOKIES['playerIdentifier']:
            team = 'blue'
        elif GameState.redGuesserId == request.COOKIES['playerIdentifier']:
            team = 'red'
        else:
            return HttpResponseForbidden('You are not allowed inside this game.')
    else:
        if GameState.blueGuesserId == request.user.id:
            team = 'blue'
        elif GameState.redGuesserId == request.user.id:
            team = 'red'
        else:
            return HttpResponseForbidden('You are not allowed inside this game.')


    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8')) # dobija se indeks 1 do 25
        action = data['action']
        if action == 'guess':

            tile_index = int(data['tileIndex'].replace("box",""))-1 # prebacuje na 0 - 24 indeks
            guessed_word = data['guessed_word']
            guessed_color = GameState.game_words[guessed_word][0]
            GameState.game_words[guessed_word][1] = 1  # Set to guessed
            print("GUESSED COLOR:", guessed_color)
            print(tile_index)

            if request.user.id != None:
                pogadjanje = Pogadjanje(user = request.user, poljeIndeks=tile_index)
                pogadjanje.save()

            if guessed_color == team:
                # Moze ponovo guess
                pass
            elif guessed_color == "black":
                # Kraj igre, tim gubi
                pass
                # TODO Render victory screen
            else:
                # Kraj poteza
                if team == 'blue':
                    GameState.turn = 4
                elif team == 'red':
                    GameState.turn = 2

        elif action == 'end_guess':
            if team == 'blue':
                GameState.turn = 4
            elif team == 'red':
                GameState.turn = 2

        # Reload se radi nakon sto stigne response od post metode
        return HttpResponse(json.dumps({"done":True}))

    context = {
        'gamestate': GameState
    }
    return render(request, 'game/guesser.html', context)


def leader(request):

    if not GameState.is_game_init:
        GameState.init_words()

    # odredjivanje tima na osnovu requesta
    if request.user.id == None:
        if GameState.blueLeaderId == request.COOKIES['playerIdentifier']:
            team = 'blue'
        elif GameState.redLeaderId == request.COOKIES['playerIdentifier']:
            team = 'red'
        else:
            return HttpResponseForbidden('You are not allowed inside this game.')
    else:
        if GameState.blueLeaderId == request.user.id:
            team = 'blue'
        elif GameState.redLeaderId == request.user.id:
            team = 'red'
        else:
            return HttpResponseForbidden('You are not allowed inside this game.')


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
            if request.user.id != None:
                asoc = Asocijacija(user=request.user, zadataRec=clue)
                asoc.save()

            if team == 'blue':
                GameState.turn = 3
            elif team == 'red':
                GameState.turn = 5

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

    # odredjivanje tima na osnovu requesta
    if request.user.id == None:
        if GameState.blueLeaderId == request.COOKIES['playerIdentifier']:
            team = 'blue'
        elif GameState.redLeaderId == request.COOKIES['playerIdentifier']:
            team = 'red'
        else:
            return HttpResponseForbidden('You are not allowed inside this game.')
    else:
        if GameState.blueLeaderId == request.user.id:
            team = 'blue'
        elif GameState.redLeaderId == request.user.id:
            team = 'red'
        else:
            return HttpResponseForbidden('You are not allowed inside this game.')

    # Logika koji igrac igra za default neka bude red
    specific_player_words = {}
    if team == "red":
        specific_player_words = {key: value for key, value in GameState.game_words.items() if value[0] == "red"}
    elif team == "blue":
        specific_player_words = {key: value for key, value in GameState.game_words.items() if value[0] == "blue"}

    context = {
        'specific_player_words': specific_player_words,
        'gamestate': GameState
    }

    return render(request, 'game/reroll.html', context)
