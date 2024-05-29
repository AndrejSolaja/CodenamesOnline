# Teodor Đelić 2021/0254
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.forms import ValidationError, Form
from home.models import Korisnik
from django.contrib.auth import get_user_model

class PasswordRecoveryForm(Form):
    """
        # TODO
    """
    def __init__(self, *args, **kwargs):
        super(PasswordRecoveryForm, self).__init__(*args, **kwargs)
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'textfield',
            'placeholder': '',
            'id': 'username_email',
            'onchange': 'updateUColors()'
        }
    ))

    class Meta:
        fields = ["username"]

class KorisnikLoginForm(AuthenticationForm):
    """
        # TODO
    """
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

class KorisnikRegisterForm(UserCreationForm):
    """
        # TODO
    """
    def __init__(self, *args, **kwargs):
        super(KorisnikRegisterForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'textfield',
            'placeholder': '',
            'id': 'username',
            'onchange': 'updateUColors()'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'textfield',
            'placeholder': '',
            'id': 'email',
            'onchange': 'updateEColors()'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'textfield',
            'placeholder': '',
            'id': 'password',
            'onchange': 'updatePColors()'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'textfield',
            'placeholder': '',
            'id': 'password_confirmed',
            'onchange': 'updatePCColors()'
        }
    ))

    def clean_username(self):  
        username = self.clean()["username"].lower()
        new = Korisnik.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User already exist")  
        return username  
  
    def clean_email(self):  
        email = self.clean()["email"].lower()  
        new = Korisnik.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Email already exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.clean()["password1"]
        password2 = self.clean()["password2"]
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password do not match")  
        return password2
    
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit = True):  
        user = Korisnik.objects.create_user(
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            password = self.cleaned_data['password1'],
            date_joined = datetime.today()
        )  
        return user 