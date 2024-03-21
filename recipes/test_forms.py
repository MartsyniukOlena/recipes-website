from django.test import TestCase
from django.shortcuts import reverse
from .forms import CommentForm, RecipeForm, SearchForm


class TestCommentForm(TestCase):
    """
    Test case for the CommentForm with valid and invalid data.
    """
    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This a test comment'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class RecipeFormTestCase(TestCase):
    """
    Test case for the RecipeForm form for all fields.
    """
    def test_form_valid_data(self):
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'content': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image':
                '/workspace/recipes-website/static/images/placeholder.jpg'
        })
        self.assertTrue(recipe_form.is_valid())

    def test_form_title_is_required(self):
        """Test for the 'title' field"""
        recipe_form = RecipeForm({
            'title': '',
            'excerpt': 'This is a test recipe',
            'content': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image':
                '/workspace/recipes-website/static/images/placeholder.jpg'
        })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")

    def test_form_excerpt_is_not_required(self):
        """Test for the 'excerpt' field"""
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'content': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image':
                '/workspace/recipes-website/static/images/placeholder.jpg'
        })
        self.assertTrue(recipe_form.is_valid())

    def test_form_content_is_required(self):
        """Test for the 'content' field"""
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'content': '',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
            'featured_image':
                '/workspace/recipes-website/static/images/placeholder.jpg'
        })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")

    def test_form_cooking_time_is_required(self):
        """Test for the 'cooking_time' field"""
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'content': 'Step 1: Do this, Step 2: Do that',
            'servings': 4,
            'status': 1,
            'featured_image':
                '/workspace/recipes-website/static/images/placeholder.jpg'
        })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")

    def test_form_servings_is_required(self):
        """Test for the 'servings' field"""
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'content': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'status': 1,
            'featured_image':
                '/workspace/recipes-website/static/images/placeholder.jpg'
        })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")

    def test_form_status_required(self):
        """Test for the 'status' field"""
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': 'This is a test recipe',
            'content': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'featured_image':
                '/workspace/recipes-website/static/images/placeholder.jpg'
        })
        self.assertFalse(recipe_form.is_valid(), msg="Form is valid")

    def test_form_featured_image_is_not_required(self):
        """Test for the 'featured_image' field"""
        recipe_form = RecipeForm({
            'title': 'Test Recipe',
            'excerpt': '',
            'content': 'Step 1: Do this, Step 2: Do that',
            'cooking_time': 30,
            'servings': 4,
            'status': 1,
        })
        self.assertTrue(recipe_form.is_valid(), msg="Form is valid")


class SearchFormTestCase(TestCase):
    """
    Test case for the SearchForm.
    """

    def test_search_form_valid_data(self):
        """
        Test whether the SearchForm is valid when provided with valid data.
        """
        search_form = SearchForm({'query': 'Test Query'})
        self.assertTrue(search_form.is_valid())

    def test_search_form_blank_data(self):
        """
        Test whether the SearchForm is invalid when provided with blank data.
        """
        search_form = SearchForm({'query': ''})
        self.assertFalse(search_form.is_valid())

    def test_search_form_max_length(self):
        """
        Test whether the SearchForm is invalid when provided with a query exceeding the maximum length.
        """
        search_form = SearchForm({'query': 'abcdfghijkslmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst uvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst'})
        self.assertFalse(search_form.is_valid())
