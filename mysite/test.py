from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from profilesite.models import Bouncer


class RedirectTests(TestCase):

    def setUp(self):
        """Notwendig da eine Art Türsteher die Erlaubnis jedem Besucher erteilen muss"""

        self.bouncer = Bouncer.objects.create(permission=True)

    def test_redirect_to_profilesite(self):
        """Testet die Weiterleitung von der Root-URL zur profilesite:index URL"""

        # Testet die Weiterleitung von der Root-URL zur profilesite:index URL
        response = self.client.get('/')
        
        # Überprüft, ob der Redirect (302 oder 301) korrekt ist
        self.assertRedirects(response, reverse('profilesite:index'), status_code=301, target_status_code=200)
