from django.test import TestCase
from django.urls import reverse
from .models import Category


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

    def test_view_without_data(self):

        """Tests whether the index page cannot be accessed without data"""

        response = self.client.get(reverse("blogs:index"))
        self.assertEqual(response.status_code, 404)

    def test_view_with_data(self):
        
        """Tests whether the index page can be accessed with data"""

        self.create_category_data("Testtitel", "Testbeschreibung")
        response = self.client.get(reverse("blogs:index"))
        self.assertGreater(response.context["cats"], [])
        self.assertEqual(response.status_code, 200)
