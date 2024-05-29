# Đorđe Vuković 2021/0327
from django.db import models
from django.contrib.auth.models import AbstractUser


class Korisnik(AbstractUser):
    """
    Stores information about logged user.
    """
    email = models.EmailField(("email address"), unique=True)
    broj_partija_leader = models.IntegerField(default=0)
    broj_pobeda_leader = models.IntegerField(default=0)
    broj_partija_guesser = models.IntegerField(default=0)
    broj_pobeda_guesser = models.IntegerField(default=0)

    class Meta:
        db_table = 'korisnik'

class Asocijacija(models.Model):
    """
    Stores hystory of given clues.
    """
    user = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    zadataRec = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'asocijacija'

class Pogadjanje(models.Model):
    """
    Stores history of guesses.
    """
    user = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    poljeIndeks = models.IntegerField(null=True)

    class Meta:
        db_table = 'pogadjanje'

class Rec(models.Model):
    """
    Stores single word.
    """
    rec = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'rec'
class SetReci(models.Model):
    """
    Stores set of words, its name, is it active, who created it, related to Rec.
    """
    naziv = models.CharField(max_length=50, unique=True, null=True)
    active = models.BooleanField(null=False, default=False)
    reci = models.ManyToManyField(Rec)
    kreator = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    class Meta:
        db_table = 'setReci'

