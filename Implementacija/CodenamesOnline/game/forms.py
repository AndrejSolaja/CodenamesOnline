# Andrej Šolaja 2021/0344
# Teodor Đelić 2021/0254
from django import forms


class ClueForm(forms.Form):
    """
    Form for giving clues on game/leader page.
    """
    clue = forms.CharField(label='Clue', max_length=100)
    clue_num = forms.IntegerField(label='Clue Number', min_value=1, max_value=9)

class TeamSelect(forms.Form):
    """
    # TODO
    """
    playerId = forms.IntegerField(min_value=0, max_value=3)