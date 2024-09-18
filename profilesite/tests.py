# test.py
from django.test import TestCase
from django.urls import reverse
from .models import Bouncer


class BouncerMiddlewareTest(TestCase):
    def setUp(self):
        """Erstelle einen Bouncer-Eintrag mit permission=False"""

        self.bouncer = Bouncer.objects.create(permission=False)

    def test_redirect_when_permission_false(self):
        """Wenn permission=False ist, sollte die Middleware auf die Landingpage umleiten"""

        response = self.client.get(reverse('profilesite:index'))
        self.assertRedirects(response, reverse('profilesite:not_ready'))

        response = self.client.get(reverse('profilesite:about'))
        self.assertRedirects(response, reverse('profilesite:not_ready'))

        response = self.client.get(reverse('profilesite:resume'))
        self.assertRedirects(response, reverse('profilesite:not_ready'))

        response = self.client.get(reverse('profilesite:projects'))
        self.assertRedirects(response, reverse('profilesite:not_ready'))

    def test_access_when_permission_true(self):
        """Setze permission auf True und teste, dass die Seiten zugänglich sind"""
        
        self.bouncer.permission = True
        self.bouncer.save()

        response = self.client.get(reverse('profilesite:index'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('profilesite:about'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('profilesite:resume'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('profilesite:projects'))
        self.assertEqual(response.status_code, 200)

    def test_not_ready_access(self):
        """Die Landingpage sollte immer zugänglich sein, unabhängig von permission"""

        response = self.client.get(reverse('profilesite:not_ready'))
        self.assertEqual(response.status_code, 200)

