from django.test import TestCase
from .models import Category, Recipe
# Create your tests here.

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(category.name, "Desserts")
        # Тестуємо наш метод __iter__
        self.assertEqual(dict(category), {'name': 'Desserts'})