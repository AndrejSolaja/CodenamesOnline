# Djordje Vukovic

from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client, SimpleTestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from game.views import *
from home.models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from game.game_state import GameState
from django.http.cookie import SimpleCookie
# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_teamSelect_is_resolved(self):
        url = reverse('teamSelect')
        self.assertEqual(resolve(url).func, teamSelect)

    def test_guesser_is_resolved(self):
        url = reverse('guesser')
        self.assertEqual(resolve(url).func, guesser)

    def test_leader_is_resolved(self):
        url = reverse('leader')
        self.assertEqual(resolve(url).func, leader)

    def test_reroll_is_resolved(self):
        url = reverse('reroll')
        self.assertEqual(resolve(url).func, reroll)

    def test_victory_is_resolved(self):
        url = reverse('victory')
        self.assertEqual(resolve(url).func, victory)

    def test_players_is_resolved(self):
        url = reverse('players')
        self.assertEqual(resolve(url).func, players)

    def test_activeSet_is_resolved(self):
        url = reverse('activeSet')
        self.assertEqual(resolve(url).func, activeSet)

class TestViews(TestCase):

    def setUp(self):


        self.client = Client()

        k = Korisnik.objects.create(username='korisnikTest')
        k.set_password('korisnikTest')
        k.save()
        s = SetReci.objects.create(naziv='Test', kreator=k)
        s.active = True
        s.save()
        wordList = ['boon', 'daughter', 'urinate', 'clash', 'outer', 'rule', 'unionize', 'castle', 'briny', 'detonate', 'dry', 'boo', 'scuff', 'tightly', 'style', 'sight', 'swap', 'resume', 'oval', 'laugh', 'truck', 'oiler', 'moved', 'meld', 'recapitulate', 'depict', 'poleaxe', 'fore', 'pure', 'recall', 'pilar']

        for word in wordList:
            r = Rec(rec=word)
            r.save()
            s.reci.add(r)



    def test_players(self):
        response = self.client.get(reverse('players'))

        self.assertEqual(response.status_code, 200)

    def test_activeSet(self):
        response = self.client.get(reverse('activeSet'))

        self.assertEqual(response.status_code, 200)

    def test_teamSelect_GET(self):

        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueLeaderId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        response = self.client.get(reverse('teamSelect'))

        self.assertEqual(response.status_code, 302)

    def test_teamSelect_POST(self):

        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueLeaderId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        response = self.client.post(reverse('teamSelect'), data={
            'playerId' : 0
        })

        self.assertEqual(response.status_code, 302)

    def test_victory_GET(self):
        response = self.client.get(reverse('victory'))

        self.assertEqual(response.status_code, 200)

    def test_guesser_GET_noWinner(self):
        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueGuesserId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        response = self.client.get(reverse('guesser'))

        self.assertEqual(response.status_code, 200)

    def test_guesser_GET_yesWinner(self):
        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueGuesserId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        GameState.winnerTeam='blue'

        response = self.client.get(reverse('guesser'))

        self.assertEqual(response.status_code, 302)
        GameState.winnerTeam = None

    def test_guesser_GET_noWinner(self):
        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueGuesserId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        response = self.client.get(reverse('guesser'))

        self.assertEqual(response.status_code, 200)

    def test_leader_GET(self):
        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueLeaderId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        response = self.client.get(reverse('leader'))

        self.assertEqual(response.status_code, 200)

    def test_leader_POST(self):
        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueLeaderId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        response = self.client.post(reverse('leader'), data={
            'clue':'dog',
            'clue_num':2
        })

        self.assertEqual(response.status_code, 302)

    def test_reroll_GET(self):
        self.client.cookies = SimpleCookie({'playerIdentifier': '6f4ab8cc-820b-4a5a-9b22-4205af544c76'})
        GameState.blueLeaderId = uuid.UUID('6f4ab8cc-820b-4a5a-9b22-4205af544c76').hex
        response = self.client.get(reverse('leader'))

        self.assertEqual(response.status_code, 200)

class FunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        service = webdriver.ChromeService(executable_path='C:\\Users\\andre\\Desktop\\PSI\\MainProjekat\\project_Imposters_Inc\\Implementacija\\CodenamesOnline\\chromedriver.exe')
        # service = webdriver.ChromeService(executable_path='C:\\Users\\Djole\\Documents\\ETF\\PSI\\project_Imposters_Inc\\Implementacija\\CodenamesOnline\\chromedriver.exe')
        self.browser = webdriver.Chrome(service = service)
        self.appUrl = self.live_server_url + "/game"

    def tearDown(self):
        self.browser.close()

    def test_teamSelect_Leader(self):
        k = Korisnik.objects.create(username='luka')
        k.set_password('Luka12345')
        k.save()

        self.browser.get(self.appUrl)

        dugme = self.browser.find_element(By.ID, "0")
        if dugme.is_enabled():
            dugme.click()
            time.sleep(5)


            self.assertEqual(self.browser.title, 'Codenames Online - Reroll Words')
        else:
            self.assertEqual(True, False)