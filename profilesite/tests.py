from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_appearance_index(self):

        """Tests whether index page appear"""

        response = self.client.get(reverse("profilesite:index"))
        self.assertEqual(response.status_code, 200)

