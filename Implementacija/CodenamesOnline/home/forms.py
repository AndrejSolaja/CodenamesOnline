from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class KorisnikLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(KorisnikLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'textfield',
            'placeholder': '',
            'id': 'username_email',
            'onchange': 'updateUColors()'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'textfield',
            'placeholder': '',
            'id': 'password',
            'onchange': 'updatePColors()'
        }
    ))