from django.shortcuts import render, get_object_or_404
from urllib3 import request

from game.game_state import GameState
from game.forms import ClueForm, TeamSelect
from home.models import *
from django.shortcuts import redirect

from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
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


def getGamerTagById(playerId):
    if playerId is None:
        return None
    
    try:
        user = Korisnik.objects.filter(id=playerId).first()
    except:
        return "Anonymous"

    if user is None:
        return "Anonymous"
    
    return user.username

def players(request):        
    return HttpResponse(
            json.dumps([getGamerTagById(GameState.redLeaderId), getGamerTagById(GameState.redGuesserId), getGamerTagById(GameState.blueLeaderId), getGamerTagById(GameState.blueGuesserId)]),
            content_type="application/json")

def activeSet(request):    
    activeSetReci = SetReci.objects.filter(active=True).first()
    return HttpResponse(
        json.dumps("DEFAULT SET" if activeSetReci is None else activeSetReci.naziv + " SET"),
        content_type="application/json"
    )

# Create your views here.
def teamSelect(request):

    REDIRECT_LINK_REROLL = "reroll"
    REDIRECT_LINK_LEADER = "leader"
    REDIRECT_LINK_GUESSER = "guesser"

    if not GameState.is_game_init:
        GameState.init_words()

    playerId = getId(request)

    if playerId != None:
        if GameState.redLeaderId == playerId:
            if GameState.turn < 1:
                return redirect(REDIRECT_LINK_REROLL)
            else:
                return redirect(REDIRECT_LINK_LEADER)
        if GameState.blueLeaderId == playerId:
            if GameState.turn < 2:
                return redirect(REDIRECT_LINK_REROLL)
            else:
                return redirect(REDIRECT_LINK_LEADER)
        elif GameState.redGuesserId == playerId or GameState.blueGuesserId == playerId:
            return redirect(REDIRECT_LINK_GUESSER)

    if request.method == "POST":

        form = TeamSelect(request.POST)

        if (form.is_valid()):
            playerId = form.cleaned_data['playerId']

            generatedId = generateId(request)

            redirectLocation = ""

            if playerId == 0:
                if GameState.redLeaderId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.redLeaderId = generatedId
                redirectLocation = REDIRECT_LINK_REROLL
            elif playerId == 1:
                if GameState.redGuesserId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.redGuesserId = generatedId
                redirectLocation = REDIRECT_LINK_GUESSER
            elif playerId == 2:
                if GameState.blueLeaderId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.blueLeaderId = generatedId
                redirectLocation = REDIRECT_LINK_REROLL
            else:
                if GameState.blueGuesserId != None:
                    return render(request, 'game/teamSelect.html')
                GameState.blueGuesserId = generatedId
                redirectLocation = REDIRECT_LINK_GUESSER

            response = redirect(redirectLocation)

            if not request.user.is_authenticated:
                response.set_cookie("playerIdentifier", generatedId)

            return response

    return render(request, 'game/teamSelect.html')


def victory(request):
    context = {
        'teamWon': GameState.winnerTeam
    }
    return render(request, 'game/victory.html', context)


def guesser(request):

    def end_turn():
        if team == 'blue':
            GameState.turn = 4
        elif team == 'red':
            GameState.turn = 2
        GameState.guess_in_row_cnt = 0

    #print(GameState.turn)

    if not GameState.is_game_init:
        GameState.init_words()

    # odredjivanje tima na osnovu requesta
    userID = getId(request)

    if userID == None:
        return HttpResponseForbidden('You are not allowed inside this game.')
    elif GameState.blueGuesserId == userID:
        team = 'blue'
    elif GameState.redGuesserId == userID:
        team = 'red'
    else:
        return HttpResponseForbidden('You are not allowed inside this game.')

    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))  # dobija se indeks 1 do 25
        action = data['action']
        if action == 'guess':

            tile_index = int(data['tileIndex'].replace("box", "")) - 1  # prebacuje na 0 - 24 indeks
            guessed_word = data['guessed_word']
            guessed_color = GameState.game_words[guessed_word][0]
            GameState.game_words[guessed_word][1] = 1  # Set to guessed
            print("GUESSED COLOR:", guessed_color)
            print(tile_index)

            if request.user.id != None:
                pogadjanje = Pogadjanje(user=request.user, poljeIndeks=tile_index)
                pogadjanje.save()

            if guessed_color == team:
                GameState.guessed_count[team] += 1
                GameState.guess_in_row_cnt += 1
                # Ukoliko je poslednji pogodak kraj je igre
                if GameState.guessed_count['blue'] == GameState.BLUE_CARD_NUM:
                    GameState.winnerTeam = 'blue'
                elif GameState.guessed_count['red'] == GameState.RED_CARD_NUM:
                    GameState.winnerTeam = 'red'
                # Moze ponovo guess posto je pogodio do maks clue_num + 1 puta
                if GameState.guess_in_row_cnt == GameState.clue_num + 1:
                    end_turn()
            elif guessed_color == "black":
                # Kraj igre, tim koji je pogodio crnu gubi
                if team == 'blue':
                    GameState.winnerTeam = 'red'
                else:
                    GameState.winnerTeam = 'blue'
                GameState.guess_in_row_cnt = 0
                # Render ce se vrsiti u get metodi nakon sto se pozove reload
            else:
                # Kraj poteza guessom na white
                end_turn()

        elif action == 'end_guess':
            end_turn()

        # Reload se radi nakon sto stigne response od post metode
        return HttpResponse(json.dumps({"done": True}))

    myTurn = False
    if (GameState.turn == 3) and (team == 'blue'):
        myTurn = True
    elif (GameState.turn == 5) and (team == 'red'):
        myTurn = True

    if GameState.winnerTeam == None:
        context = {
            'gamestate': GameState,
            'myTurn': myTurn,
        }
        return render(request, 'game/guesser.html', context)
    else:
        # Update baze korisnika u zavisnosti od toga da li je pobedio ili ne
        if request.user.id != None:
            kor = Korisnik.objects.get(id=request.user.id)
            if team == GameState.winnerTeam:
                kor.broj_pobeda_guesser +=1
            kor.broj_partija_guesser +=1
            kor.save()

        return redirect('victory')


def leader(request):
    print(GameState.turn)

    if not GameState.is_game_init:
        GameState.init_words()

    # odredjivanje tima na osnovu requesta
    userID = getId(request)

    if userID == None:
        return HttpResponseForbidden('You are not allowed inside this game.')
    elif GameState.blueLeaderId == userID:
        team = 'blue'
    elif GameState.redLeaderId == userID:
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

            # Dodati clues u game state da bi mogli da se dohvate kod Guessera
            if team == 'blue':
                GameState.blue_clues.append(clue + ', ' + str(clue_num))
            else:
                GameState.red_clues.append(clue + ', ' + str(clue_num))

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

    if GameState.winnerTeam == None:
        context = {
            'gamestate': GameState,
            'form': form,
            'myTurn': myTurn
        }
        return render(request, 'game/leader.html', context)
    else:
        # Update baze korisnika u zavisnosti od toga da li je pobedio ili ne
        if request.user.id != None:
            kor = Korisnik.objects.get(id=request.user.id)
            if team == GameState.winnerTeam:
                kor.broj_pobeda_leader +=1
            kor.broj_partija_leader +=1
            kor.save()
        return redirect('victory')


def reroll(request):
    if not GameState.is_game_init:
        GameState.init_words()

    # odredjivanje tima na osnovu requesta
    userID = getId(request)

    if userID == None:
        return HttpResponseForbidden('You are not allowed inside this game.')
    elif GameState.blueLeaderId == userID:
        team = 'blue'
    elif GameState.redLeaderId == userID:
        team = 'red'
    else:
        return HttpResponseForbidden('You are not allowed inside this game.')

    # Logika koji igrac igra za default neka bude red
    specific_player_words = {}
    if team == "red":
        specific_player_words = {key: value for key, value in GameState.game_words.items() if value[0] == "red"}
    elif team == "blue":
        specific_player_words = {key: value for key, value in GameState.game_words.items() if value[0] == "blue"}

    myTurn = False
    if (GameState.turn == 0) and (team == 'blue'):
        myTurn = True
    elif (GameState.turn == 1) and (team == 'red'):
        myTurn = True

    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        new_words = data['new_words']
        old_words = data['old_words']
        print('new_words:', new_words)
        print('old_words:', old_words)

        for i in range(len(new_words)):
            del GameState.game_words[old_words[i]]
            GameState.game_words[new_words[i]] = [team, 0]
            GameState.remaining_words.remove(new_words[i])

        if team == 'blue' and GameState.turn == 0:
            GameState.turn = 1
        elif team == 'red' and GameState.turn == 1:
            GameState.turn = 2
        return JsonResponse({'success': True, 'redirect_url': 'leader'})

    context = {
        'specific_player_words': specific_player_words,
        'gamestate': GameState,
        'myTurn': myTurn
    }

    return render(request, 'game/reroll.html', context)
