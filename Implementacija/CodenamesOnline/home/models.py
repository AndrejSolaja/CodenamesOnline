from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Korisnik(AbstractUser):
    email = models.EmailField(("email address"), unique=True)
    broj_partija_leader = models.IntegerField(default=0)
    broj_pobeda_leader = models.IntegerField(default=0)
    broj_partija_guesser = models.IntegerField(default=0)
    broj_pobeda_guesser = models.IntegerField(default=0)

    class Meta:
        db_table = 'korisnik'

class Asocijacija(models.Model):
    user = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    zadataRec = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'asocijacija'

class Pogadjanje(models.Model):
    user = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    poljeIndeks = models.IntegerField(null=True)

    class Meta:
        db_table = 'pogadjanje'

class Rec(models.Model):
    rec = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'rec'
class SetReci(models.Model):
    naziv = models.CharField(max_length=50, unique=True, null=True)
    reci = models.ManyToManyField(Rec)
    class Meta:
        db_table = 'setReci'

