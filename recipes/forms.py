from django import forms
from django.core.validators import MaxLengthValidator
from .models import Comment, Recipe

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'excerpt', 'content', 'cooking_time', 'servings', 'status', 'featured_image']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, validators=[MaxLengthValidator(100)])