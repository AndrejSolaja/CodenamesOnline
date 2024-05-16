from django import forms


class ClueForm(forms.Form):
    clue = forms.CharField(label='Clue', max_length=100)
    clue_num = forms.IntegerField(label='Clue Number', min_value=1, max_value=9)
