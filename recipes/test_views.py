from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Recipe

class TestRecipeViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.recipe = Recipe(title="Recipe title", author=self.user,
                         slug="recipe-title", excerpt="Recipe excerpt",
                         content="Recipe content", cooking_time=1, servings=2, status=1)
        self.recipe.save()


    def test_render_recipe_detail_page_with_comment_form(self):
        """Verifies a single recipe page containing a comment form is returned"""
        response = self.client.get(reverse('recipe_detail', args=['recipe-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recipe title", response.content)
        self.assertIn(b"Recipe content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)


    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('recipe_detail', args=['recipe-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval',
                      response.content)


    def test_successful_recipe_submission(self):
        """Test for posting a recipe"""
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(reverse('add_recipe'), {'title': 'New Recipe', 'content': 'Step 1: Do this, Step 2: Do that', 'cooking_time': 30,
            'servings': 4, 'status': 1})
        self.assertEqual(response.status_code, 302)


    def test_favorite_recipes_view(self):
        """Test for rendering a page to display recipes added to Favorities"""
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse('favorite_recipes'))
        self.assertEqual(response.status_code, 200) 


    def test_add_to_favorites_view(self):
        """Test for adding recipes to Favorities"""
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.post(reverse('add_to_favorites', kwargs={'slug': self.recipe.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Recipe added to Favorites')


    def test_remove_from_favorites_view(self):
        """Test for removing recipes from Favorities"""
        self.client.login(username="myUsername", password="myPassword")
        self.user.favorite.add(self.recipe)
        response = self.client.post(reverse('remove_from_favorites', kwargs={'slug': self.recipe.slug}))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json()['message'], 'Recipe removed from Favorites')