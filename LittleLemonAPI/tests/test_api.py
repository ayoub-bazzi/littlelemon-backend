from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse

from LittleLemonAPI.models import Booking, MenuItem

class MenuTests(APITestCase):
    def setUp(self):
        MenuItem.objects.create(title='Pizza', price=12.5, inventory=10)

    def test_menu_list_public(self):
        url = reverse('menuitem-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 1)


class BookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_booking_requires_auth(self):
        self.client.credentials()  # remove token
        url = reverse('booking-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 401)

    def test_booking_create_authenticated(self):
        url = reverse('booking-list')
        data = {
            'booking_date':'2025-09-10',
            'booking_time':'19:00:00',
            'party_size':4
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['user'], 'test')


class UserTests(APITestCase):
    def test_user_registration_returns_token(self):
        url = reverse('registration-register')
        data = {'username':'newuser','password':'pass123','email':'test@example.com'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        self.assertIn('token', resp.data)

    def test_token_login_returns_token(self):
        user = User.objects.create_user(username='loginuser', password='pass123')
        url = '/api/api-token-auth/'
        data = {'username':'loginuser','password':'pass123'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('token', resp.data)
