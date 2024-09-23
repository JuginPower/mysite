from django.test import TestCase
from django.urls import reverse
from .models import Category
from profilesite.models import Bouncer


class CategoryData():

    def create_category_data(self, name, description) -> Category:

        """Creates an object of type Category in the database and returns the 
        stored object"""

        category = Category(name=name, description=description)
        category.save()
        saved_category = Category.objects.get(id=category.id)
        return saved_category


class CategoryModelTest(TestCase, CategoryData):

    def test_category_save(self):

        """Tests whether you can successfully store data of type Category in 
        the database"""

        name = "Testtitel"
        description = "Eine Testbeschreibung"
        saved_category = self.create_category_data(name, description)

        self.assertEqual(saved_category.name, name)
        self.assertEqual(saved_category.description, description)


class IndexViewTest(TestCase, CategoryData):

    def setUp(self):
        self.bouncer = Bouncer.objects.create(purpose="bl",permission=True)

    def test_view_without_data(self):

        """Tests whether the index page cannot be accessed without data"""

        response = self.client.get(reverse("blogs:index"))
        # print("Response Url:", response.url)
        self.assertEqual(response.status_code, 404)

    def test_view_with_data(self):
        
        """Tests whether the index page can be accessed with data"""

        self.create_category_data("Testtitel", "Testbeschreibung")
        response = self.client.get(reverse("blogs:index"))
        self.assertGreater(response.context["cats"], [])
        self.assertEqual(response.status_code, 200)


class BouncerTest(TestCase, CategoryData):
    def setUp(self):
        """Erstelle einen Bouncer-Eintrag mit permission=False und eine Category Objekt"""

        self.bouncer = Bouncer.objects.create(purpose="bl",permission=False)
        self.create_category_data("Testtitel", "Testbeschreibung")

    def test_redirect_when_permission_false(self):
        """Wenn permission=False ist, soll auf die Landingpage umgeleitet werden"""

        response = self.client.get(reverse('blogs:index'))
        self.assertRedirects(response, reverse('blogs:not_ready'))

    def test_access_when_permission_true(self):
        """Setze permission auf True und teste, dass die Seiten zugänglich sind"""
        
        self.bouncer.permission = True
        self.bouncer.save()

        response = self.client.get(reverse('blogs:index'))
        self.assertEqual(response.status_code, 200)


    def test_not_ready_access(self):
        """Die Landingpage sollte immer zugänglich sein, unabhängig von permission"""

        response = self.client.get(reverse('blogs:not_ready'))
        self.assertEqual(response.status_code, 200)