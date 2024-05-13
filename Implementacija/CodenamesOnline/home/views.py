from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from home.forms import KorisnikLoginForm

from home.models import *

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def logout_req(request):
    logout(request)
    return redirect('home')

def login_req(request):
    """
    Display a login page and authenticate user :model:`CodenamesOnline.Korisnik`.

    **Context**

    ``form``
        A login form.
    ``errorMessage``
        An error message to be displayed.

    **Template:**

    :template:`CodenamesOnline/templates/home/login.html`
    """
    if request.method == "POST":

        form = KorisnikLoginForm(request = request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user is None:
                
                context = {
                'errorMessage': "Credentials are invalid.",
                'form': form
                }

                return render(request, 'home/login.html', context)
            else:
                login(request,user)
                return redirect('home')
        else:
            context = {
                'errorMessage': "Credentials are invalid.",
                'form': form
                }

            return render(request, 'home/login.html', context)
                
    else:
        form = KorisnikLoginForm()

        context = {
            'form': form
        }

        return render(request, 'home/login.html', context)

def newset(request):
    if request.method=="POST":
        words = request.POST['words_input']
        wordList = words.split(',')
        setName = request.POST['name_input']

        # provera da li u bazi postoji ime koje je zadato
        listaSetovaReciIstogImena = SetReci.objects.filter(naziv=setName).all()
        if len(listaSetovaReciIstogImena) > 0:
            # Vec postoji to ime
            context = {
                'setName': setName,
                'words' : words,
                'name_error': 'There already exists a set with that name.',
            }

            return render(request, 'home/newSet.html', context)
        elif setName == "":
            # Nije uneto ime seta
            context = {
                'setName': setName,
                'words': words,
                'name_error': 'There is no set name. Please enter a name for you word set.',
            }

            return render(request, 'home/newSet.html', context)
        elif len(wordList) < 31:
            # Nije uneto dovoljno reci, ostaviti mu upisane
            context = {
                'setName': setName,
                'words': words,
                'word_error': 'Not enough words! The minimum is 31.',
            }

            return render(request, 'home/newSet.html', context)
        else:
            # Sve u redu, sacuvati info u bazi

            s = SetReci(naziv=setName)
            s.save()

            # Cuvamo reci u bazi -> tek nakon sto je rec sacuvana moze da se poveze sa setom Reci
            for word in wordList:
                r = Rec(rec = word)
                r.save()
                s.reci.add(r)

            context = {
                'setNameSuccess': setName,
                'success_msg' : ' set was successfully created!',
                'name_error':'',
                'word_error': '',
            }

            return render(request, 'home/newSet.html', context)
    else:

        return render(request, 'home/newSet.html')

def profile(request):

    # dohvatanje ID korisnika
    korisnik = Korisnik.objects.filter(username=request.user.username).first()

    # izracunavanje i zaokruzivanje korisnickog Win Rate za obe uloge iz baze
    if korisnik.broj_pobeda_leader == 0:
        winRateL = 0
    else:
        winRateL = int(korisnik.broj_pobeda_leader /korisnik.broj_partija_leader * 100)

    if korisnik.broj_pobeda_guesser == 0:
        winRateG = 0
    else:
        winRateG = int(korisnik.broj_pobeda_guesser / korisnik.broj_partija_guesser * 100)

    # izdvajanja omiljene reci iz baze
    listaAsocijacija = Asocijacija.objects.filter(user_id = korisnik.id).all()
    listaReci = [str(x.zadataRec) for x in listaAsocijacija]
    if len(listaReci) > 0:
        najcescaRec = max(listaReci, key=listaReci.count)
    else:
        najcescaRec = ''


    # izdvajanje omiljenog polja za pogadjanje iz baze
    listaPolja = Pogadjanje.objects.filter(user_id = korisnik.id).all()
    listaIndeks = [x.poljeIndeks for x in listaPolja]
    if len(listaIndeks) > 0:
        najcesciIndeks = max(listaIndeks, key=listaIndeks.count)
    else:
        najcesciIndeks = -1

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