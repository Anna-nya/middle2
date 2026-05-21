from django.test import TestCase
from .models import Category, Recipe
# Create your tests here.

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(category.name, "Desserts")
        # Тестуємо наш метод __iter__
        self.assertEqual(dict(category), {'name': 'Desserts'})

class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        category = Category.objects.create(name="Main Course")
        recipe = Recipe.objects.create(
            title="Pasta",
            description="Delicious pasta",
            instructions="Boil water...",
            ingredients="Pasta, salt, water",
            category=category
        )
        self.assertEqual(recipe.title, "Pasta")
        self.assertEqual(recipe.category.name, "Main Course")