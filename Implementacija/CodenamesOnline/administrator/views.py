from django.http import Http404
from django.shortcuts import render, redirect
from home.models import *
# Create your views here.

def adminPage(request):
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

def adminSetEditor(request, set_id):

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

                print(set.naziv)
                print(request.POST['set_name'])

                print(request.POST['set_words'])
                print(setWords)

                if (set.naziv != request.POST['set_name']) or (setWords != request.POST['set_words']):
                    set = SetReci.objects.filter(id=set_id)
                    # TODO: provera da li postoji ovo ime u bazi
                    set.update(naziv=request.POST['set_name'])

                    set = set.first()
                    # Brisanje reci iz baze
                    reciZaBrisanje = set.reci.all()
                    reciZaBrisanje.delete()
                    set.reci.clear()

                    # dodavanje reci iz forme
                    # TODO: Provera da li postoji dovoljno unetih reci
                    wordList = request.POST['set_words'].split(',')
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
                        'set_words': setWords
                    }

                    return render(request, 'administrator/adminPageEditor.html', context)
                else:
                    #TODO: Ne primenjuje se nijedna promena, nije uneta nijedna promena

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
        elif 'delete_set' in request.POST:
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