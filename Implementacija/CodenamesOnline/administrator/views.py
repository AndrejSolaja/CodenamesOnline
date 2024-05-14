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