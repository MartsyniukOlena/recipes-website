from .models import Comment, Recipe
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'excerpt', 'ingredients', 'instructions', 'cooking_time', 'servings', 'status']