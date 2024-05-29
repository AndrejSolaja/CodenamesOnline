# Đorđe Vuković 2021/0327
# Teodor Đelić 2021/0254
from typing import LiteralString
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from home.forms import KorisnikRegisterForm, KorisnikLoginForm, PasswordRecoveryForm
from home.models import *
from django.core.mail import send_mail
from django.conf import settings

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import string
import secrets



def home(request):
    """
    Display the home page for the website. This is where every user group starts. Any user can decide to press play and join the game.
    The header is dynamic, and changes based on whether a user is logged in or not.

    **Template:**

    :template:`CodenamesOnline/templates/home/index.html`
    """
    return render(request, 'home/index.html')

def logout_req(request):
    logout(request)
    return redirect('home')

def login_req(request):
    """
    Display a login page and authenticate user :model:`home.Korisnik`.

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

                if user.is_superuser:
                    return redirect('administrator/')
                else:
                    return redirect('home')
        else:
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                try:
                    validate_email(username)
                    user = Korisnik.objects.filter(email=username).first()

                    if user is not None:
                        username = user.username
                except ValidationError:
                    pass                               

                user = authenticate(username = username, password = password)

                if user is not None:
                    login(request,user)

                    if user.is_superuser:
                        return redirect('administrator/')
                    else:
                        return redirect('home')             

            except:
                pass

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

@login_required(login_url='login')
def newset(request):
    """
    Display a page for creating a new :model:`home.SetReci`. It has a form with 2 input areas with its constraints written on the page.

    **Context**

    ``setName``
        User input text field for :model:`home.SetReci`.naziv
    ``words``
        User input text area for :model:`home.SetReci`.reci
    ``name_error``
        Displays a message if the setName already exists in the databasae, or if it wasn't filled out in the form.
    ``word_error``
        Displays a message if there are less than 31 words, separated by a comma, written in the words text area.
    ``success_msg``
        Displays a message for a successful creation of a new :model:`home.SetReci`
    ``setNameSuccess``
        Displays the name of the successfully created :model:`home.SetReci`
    **Template:**

    :template:`CodenamesOnline/templates/home/newSet.html`
    """
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

            s = SetReci(naziv=setName, kreator=request.user)
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

@login_required(login_url='login')
def profile(request):
    """
    Display a user specific profile page. The information which the user can see is: Winning percentage when playig as a leader, Winning percentage when playig as a guesser, Favorite clue word and a Favorite tile to guess.
    Admin can use this page to re-enter his /administrator page.
    A different profile page is based on which user is currently logged in when it was entered.

    **Context**

            'winRateLeader':winRateL,
            'winRateGuesser':winRateG,
            'favoriteTile' : najcesciIndeks,
            'favoriteWord':najcescaRec
    ``winRateLeader``
        Displayes a circle representing the winning percentage when playig as a leader.
    ``winRateGuesser``
        Displayes a circle representing the winning percentage when playig as a guesser.
    ``favoriteWord``
        Displays a word which was used the most times for giving a clue to the guesser.
    ``favoriteTile``
        Displays a picture of the 5x5 board, where the highlighted tile is considered the favorite, based on the amount of times it was guessed.

    **Template:**

    :template:`CodenamesOnline/templates/home/profile.html`
    """
    # dohvatanje ID korisnika
    korisnik = Korisnik.objects.filter(username=request.user.username).first()

    if korisnik.is_superuser == 1:
        return redirect('adminPage')
    else:
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
    """
    Display a password recovery page, reset password of user :model:`home.Korisnik` and send a mail with the user's new password to the user's email address.

    **Context**

    ``form``
        A password recovery form.
    ``errorMessage``
        An error message to be displayed.

    **Template:**

    :template:`CodenamesOnline/templates/home/recovery.html`
    """
    if request.method == "POST":

        user = Korisnik.objects.filter(username=request.POST["username"]).first()

        if user is None:
            context = {
                'form': PasswordRecoveryForm(),
                'errorMessage': "User does not exist"
            }

            return render(request, 'home/recovery.html', context=context)
        
        newPassword = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(16))

        plainMessage = f"Hi {user.get_username()}!\n\nYour new password is {newPassword}.\n\nKind regards,\nTeam at Codenames,\nImposters Inc."
        htmlMessage = f"<header><h2>Hi {user.get_username()}!</h2></header><br><main>Your new password is {newPassword}</main><br><footer>Kind regards,<br>Team at Codenames,<br>Imposters Inc.</footer>"

        send_mail(subject="[CodeNames] Password recovery", message=plainMessage, html_message=htmlMessage, from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email])

        user.set_password(newPassword)
        user.save()

        return redirect('home')
    
    context = {
        'form': PasswordRecoveryForm()
    }

    return render(request, 'home/recovery.html', context=context)

def register(request):
    """
    Display a registration page and create a new user :model:`home.Korisnik`.

    **Context**

    ``form``
        A registration form.
    ``errorMessages``
        Error messages to be displayed.

    **Template:**

    :template:`CodenamesOnline/templates/home/register.html`
    """
    if request.method=="POST":
        form = KorisnikRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            login(request, Korisnik.objects.filter(username=form.clean()["username"]).first())

            return redirect('home')
        else:

            errorMessages = form['password2'].errors.as_text().split("*")

            context = {
                'form': form,
                'errorMessages':  errorMessages,
            }

            return render(request, 'home/register.html', context)
    else:
        form = KorisnikRegisterForm()

        context = {
            'form': form
        }

        return render(request, 'home/register.html', context)

def rules(request):
    return render(request, 'home/rules.html')