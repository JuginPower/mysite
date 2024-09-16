from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def test_appearance_index(self):

        """Tests whether index page appear"""

        response = self.client.get(reverse("profilesite:index"))
        self.assertEqual(response.status_code, 200)


class AboutViewTest(TestCase):

    def test_appearance_index(self):

        """Tests whether about page appear"""

        response = self.client.get(reverse("profilesite:about"))
        self.assertEqual(response.status_code, 200)


class ResumeViewTest(TestCase):

    def test_appearance_index(self):

        """Tests whether resume page appear"""

        response = self.client.get(reverse("profilesite:resume"))
        self.assertEqual(response.status_code, 200)


class ProjectsViewTest(TestCase):

    def test_appearance_index(self):

        """Tests whether index page appear"""

        response = self.client.get(reverse("profilesite:projects"))
        self.assertEqual(response.status_code, 200)

