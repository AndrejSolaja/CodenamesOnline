from django import forms


class ClueForm(forms.Form):
    clue = forms.CharField(label='Clue', max_length=100)
    clue_num = forms.IntegerField(label='Clue Number', min_value=1, max_value=9)

class TeamSelect(forms.Form):
    playerId = forms.IntegerField(min_value=0, max_value=3)