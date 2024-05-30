from django.http import Http404
from django.shortcuts import render, redirect
from home.models import *
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

@user_passes_test(lambda u: u.is_superuser, login_url='login')
def adminPage(request):
    """
    Displays main page for the admin. He can choose which :model:`home.SetReci' to edit.

    **Context**

    ``activeSet``
        SetReci which is active and is going to be used to generate words for the game.
    ``sets``
        Every SetReci in the database, displayed in a clickable list.

    **Template:**

    :template:`administrator/adminPage.html`
    """
    sets = SetReci.objects.all()
    activeSet = SetReci.objects.filter(active=True).first()

    if request.method == 'POST':
        # Detekcija koje dugme je bilo pritisnuto iz liste po value, tj nazivu seta
        selectedSet = SetReci.objects.filter(naziv=request.POST['select_set']).first()
        return redirect('adminSetEditor', set_id = int(selectedSet.id))
    else:
        sets = SetReci.objects.all()
        activeSet = SetReci.objects.filter(active=True).first()

        context = {
            'activeSet': activeSet,
            'sets':sets
        }

        return render(request, 'administrator/adminPage.html', context)
@user_passes_test(lambda u: u.is_superuser, login_url='login')
def adminSetEditor(request, set_id):
    """
    Displays :model:`home.SetReci', its words and its name. The admin can edit its name and words.
    Admin can choose which set to activate for the upcoming games.

    **Context**

    ``activeSet``
        SetReci which is active and is going to be used to generate words for the game.
    ``sets``
        Every SetReci in the database, displayed in a clickable list.
    ``selected_set``
        The changes are being made to the set who's name was previously selected from the list. Its ID is in the url.
    ``set_name``
        Selected set's name.
    ``set_words``
        Selected set's words.
    ``error_message``
        In case of an invalid input (too few words, or there already exists a set with that name) a message is displayed underneath the form.
    ``success_messsage``
        In case of a properly applied change, a message is displayed in green signifying a successful change.

    **Template:**

    :template:`administrator/adminPageEditor.html`
    """
    if request.method == 'POST':
        if 'activate_set' in request.POST: #request.POST['activate_set'][0] == 'ACTIVATE'
            try:
                set = SetReci.objects.filter(id=set_id)
                sets = SetReci.objects.all()
                # Update radi samo na QuerySet !!!

                # Promeni aktivnog na False
                activeSet = SetReci.objects.filter(active=True)
                activeSet.update(active=False)
                # Postaviti trenutnog/selektovanog na active
                set.update(active=True)

                # Vratiti na administrator home page jer ne mogu da se menjaju reci aktivnog seta
                return redirect('adminPage')

            except SetReci.DoesNotExist:
                raise Http404("Set does not exist")
        elif 'change_set' in request.POST:
            try:
                set = SetReci.objects.get(id=set_id)
                sets = SetReci.objects.all()
                activeSet = SetReci.objects.filter(active=True).first()
                setWords = [x.rec for x in set.reci.all()]
                setWords = ','.join(setWords)

                if (set.naziv != request.POST['set_name']) or (setWords != request.POST['set_words']):
                    set = SetReci.objects.filter(id=set_id)
                    # provera da li postoji ovo ime u bazi, a promenjeno je
                    if (set.first().naziv != request.POST['set_name']) and (len(SetReci.objects.filter(naziv=request.POST['set_name'])) > 0):
                        context = {
                            'activeSet': activeSet,
                            'sets': sets,
                            'selected_set': set_id,
                            'set_name': set.first().naziv,
                            'set_words': setWords,
                            'error_message':'There already exists a set with that name.'
                        }
                        return render(request, 'administrator/adminPageEditor.html', context)

                    set.update(naziv=request.POST['set_name'])

                    set = set.first()


                    # dodavanje reci iz forme
                    # Provera da li postoji dovoljno unetih reci
                    wordList = request.POST['set_words'].split(',')

                    if len(wordList) < 31:
                        context = {
                            'activeSet': activeSet,
                            'sets': sets,
                            'selected_set': set_id,
                            'set_name': set.naziv,
                            'set_words': ','.join(wordList),
                            'error_message': 'Not enough words! The minimum is 31.'
                        }

                        return render(request, 'administrator/adminPageEditor.html', context)

                    # Brisanje reci iz baze
                    reciZaBrisanje = set.reci.all()
                    reciZaBrisanje.delete()
                    set.reci.clear()
                    for word in wordList:
                        r = Rec(rec = word)
                        r.save()
                        set.reci.add(r)

                    setWords = [x.rec for x in set.reci.all()]
                    setWords = ','.join(setWords)

                    context = {
                        'activeSet': activeSet,
                        'sets': sets,
                        'selected_set': set_id,
                        'set_name': set.naziv,
                        'set_words': setWords,
                        'success_message':"Successfully applied changes!"
                    }

                    return render(request, 'administrator/adminPageEditor.html', context)
                else:
                    # Ne primenjuje se nijedna promena, nije uneta nijedna promena

                    context = {
                        'activeSet': activeSet,
                        'sets': sets,
                        'selected_set': set_id,
                        'set_name': set.naziv,
                        'set_words': setWords,
                        'error_message': "You didn't make any changes."
                    }

                    return render(request, 'administrator/adminPageEditor.html', context)
            except SetReci.DoesNotExist:
                raise Http404("Set does not exist")
        elif 'delete_set' in request.POST:

            try:
                set = SetReci.objects.filter(id=set_id)

                reci = set.first().reci.all()
                reci.delete()
                set.first().reci.clear()
                set.delete()

                return redirect('adminPage')
            except SetReci.DoesNotExist:
                raise Http404("Set does not exist")
        else:
            # Detekcija koje dugme je bilo pritisnuto iz liste po value, tj nazivu seta
            selectedSet = SetReci.objects.filter(naziv=request.POST['select_set']).first()

            # Pri post metodi ispitati  da li se kliknulo na isto dugme, ono koje je vec selektovano, renderovati istu stranicu
            if selectedSet.id != set_id:
                return redirect('adminSetEditor', set_id = selectedSet.id)
            else:
                try:
                    set = SetReci.objects.get(id=set_id)
                    sets = SetReci.objects.all()
                    activeSet = SetReci.objects.filter(active=True).first()
                    setWords = [x.rec for x in set.reci.all()]
                    setWords = ','.join(setWords)

                    context = {
                        'activeSet': activeSet,
                        'sets': sets,
                        'selected_set': set_id,
                        'set_name': set.naziv,
                        'set_words': setWords
                    }

                    return render(request, 'administrator/adminPageEditor.html', context)
                except SetReci.DoesNotExist:
                    raise Http404("Set does not exist")
    else:
        try:
            set = SetReci.objects.get(id=set_id)
            sets = SetReci.objects.all()
            activeSet = SetReci.objects.filter(active=True).first()
            setWords = [x.rec for x in set.reci.all()]
            setWords = ','.join(setWords)

            context = {
                'activeSet': activeSet,
                'sets':sets,
                'selected_set': set_id,
                'set_name' : set.naziv,
                'set_words' : setWords
            }


            return render(request, 'administrator/adminPageEditor.html', context)
        except SetReci.DoesNotExist:
            raise Http404("Set does not exist")