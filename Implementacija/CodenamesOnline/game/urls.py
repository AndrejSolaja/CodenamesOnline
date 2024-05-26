
from django.urls import path, include
from game.views import teamSelect,guesser, leader, reroll, victory, players

urlpatterns = [
    path('', teamSelect, name='teamSelect'),
    path('guesser', guesser, name='guesser'),
    path('leader', leader, name='leader'),
    path('reroll', reroll, name='reroll'),
    path('victory', victory, name='victory'),
    path('players', players, name='players'),
]