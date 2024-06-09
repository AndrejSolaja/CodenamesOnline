# Andrej Solaja

from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client, SimpleTestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from game.views import *
from home.views import *
from home.models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from game.game_state import GameState
from django.http.cookie import SimpleCookie
# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_login_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_req)

    def test_recovery_is_resolved(self):
        url = reverse('recovery')
        self.assertEqual(resolve(url).func, recovery)

    def test_register_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_rules_is_resolved(self):
        url = reverse('rules')
        self.assertEqual(resolve(url).func, rules)

    def test_logout_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_req)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        k = Korisnik.objects.create(username='korisnikTest')
        k.set_password('korisnikTest')
        k.save()


    def test_login_GET(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_POST_pass(self):
        response = self.client.post(reverse('login'), data={
            'username': 'korisnikTest',
            'password': 'korisnikTest'
        })

        self.assertEqual(response.status_code, 302)

    def test_login_POST_fail(self):
        response = self.client.post(reverse('login'), data={
            'username': 'korisnikTestfail',
            'password': 'korisnikTestfail'
        })

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 302)


    def test_rules(self):
        response = self.client.get(reverse('rules'))
        self.assertEqual(response.status_code, 200)

    def test_recovery_GET(self):
        response = self.client.get(reverse('recovery'))
        self.assertEqual(response.status_code, 200)

    def test_recovery_POST(self):
        response = self.client.post(reverse('recovery'), data={
            'username': 'korisnikTest'
        })

        self.assertEqual(response.status_code, 302)

    def test_register_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_POST_pass(self):
        response = self.client.post(reverse('register'), data={
            "username": "noviKorisnik",
            "email": "testmail@gmail.com",
            "password1": "NoviKorisnik123",
            "password2": "NoviKorisnik123"
        })
        self.assertEqual(response.status_code, 302)

    def test_register_POST_fail(self):
        response = self.client.post(reverse('register'), data={
            "username": "noviKorisnik",
            "email": "testmail@gmail.com",
            "password1": "NoviKorisnik123",
            "password2": "NoviKorisnik1234"
        })
        self.assertEqual(response.status_code, 200)

class FunctionalTestCase(StaticLiveServerTestCase):

    def setUp(self):
        # service = webdriver.ChromeService(executable_path='C:\\Users\\Djole\\Documents\\ETF\\PSI\\project_Imposters_Inc\\Implementacija\\CodenamesOnline\\chromedriver.exe')
        service = webdriver.ChromeService(executable_path='C:\\Users\\andre\\Desktop\\PSI\\MainProjekat\\project_Imposters_Inc\\Implementacija\\CodenamesOnline\\chromedriver.exe')
        self.browser = webdriver.Chrome(service = service)
        self.appUrl = self.live_server_url + "/login"

    def tearDown(self):
        self.browser.close()

    def test_login(self):
        k = Korisnik.objects.create(username='korisnikTest')
        k.set_password('korisnikTest123')
        k.save()

        self.browser.get(self.appUrl)
        self.browser.find_element(By.ID, "username_email").send_keys("korisnikTest")
        self.browser.find_element(By.ID, "password").send_keys("korisnikTest123")

        dugme = self.browser.find_element(By.ID, "0")
        dugme.click()
        self.assertNotEqual(self.browser.current_url, self.live_server_url + "/login")
