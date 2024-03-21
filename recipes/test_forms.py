from django.test import TestCase
from django.shortcuts import reverse
from .forms import CommentForm, RecipeForm, SearchForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This a test comment'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")



class RecipeFormTestCase(TestCase):
    
    def test_form_valid_data(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertTrue(recipe_form.is_valid())


    def test_form_title_is_required(self):
        recipe_form = RecipeForm({
            'title': '',
            'excerpt': 'This is a test recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")


    def test_form_excerpt_is_not_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertTrue(recipe_form.is_valid())

    def test_form_ingredients_is_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'ingredients': '',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")

    def test_form_ingredients_is_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'ingredients': '',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")


    def test_form_instructions_is_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'ingredients': 'Step 1: Do this, Step 2: Do that',
            'instructions': '',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")


    def test_form_cooking_time_is_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'servings': 4,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")

    def test_form_servings_is_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'status': 1,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")


    def test_form_status_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'featured_image': '/workspace/recipes-website/static/images/placeholder.jpg'
    })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")


    def test_form_featured_image_is_not_required(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'instructions': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
    })
        self.assertTrue(recipe_form.is_valid(), msg="Form is valid")



class SearchFormTestCase(TestCase):

    def test_search_form_valid_data(self):
        search_form = SearchForm({'query': 'Test Query'})
        self.assertTrue(search_form.is_valid())


    def test_search_form_blank_data(self):
        search_form = SearchForm({'query': ''})
        self.assertFalse(search_form.is_valid())


    def test_search_form_max_length(self):
        search_form = SearchForm({'query': 'abcdfghijkslmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst'})
        self.assertFalse(search_form.is_valid())