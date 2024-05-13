from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from home.models import *

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def logout_req(request):
    logout(request)
    return redirect('home')

def login_req(request):
    return render(request, 'home/login.html')

def newset(request):
    if request.method=="POST":
        pass
    else:

        return render(request, 'home/newSet.html')

def profile(request):

    # dohvatanje ID korisnika
    korisnik = Korisnik.objects.filter(username=request.user.username).first()

    # izracunavanje i zaokruzivanje korisnickog Win Rate za obe uloge iz baze
    winRateL = int(korisnik.broj_pobeda_leader /korisnik.broj_partija_leader * 100)
    winRateG = int(korisnik.broj_pobeda_guesser / korisnik.broj_partija_guesser * 100)

    # izdvajanja omiljene reci iz baze
    listaAsocijacija = Asocijacija.objects.filter(user_id = korisnik.id).all()
    listaReci = [str(x.zadataRec) for x in listaAsocijacija]
    najcescaRec = max(listaReci, key=listaReci.count)

    # izdvajanje omiljenog polja za pogadjanje iz baze
    listaPolja = Pogadjanje.objects.filter(user_id = korisnik.id).all()
    listaIndeks = [x.poljeIndeks for x in listaPolja]
    najcesciIndeks = max(listaIndeks, key=listaIndeks.count)

    context = {
        'winRateLeader':winRateL,
        'winRateGuesser':winRateG,
        'favoriteTile' : najcesciIndeks,
        'favoriteWord':najcescaRec
    }
    return render(request, 'home/profile.html', context)

def recovery(request):
    return render(request, 'home/recovery.html')

def register(request):
    return render(request, 'home/register.html')

def rules(request):
    return render(request, 'home/rules.html')