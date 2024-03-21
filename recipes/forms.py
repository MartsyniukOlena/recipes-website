from django import forms
from django.core.validators import MaxLengthValidator
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a recipe
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Form class for users to post a recipe on the website
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Recipe
        fields = ['title', 'excerpt', 'content', 'cooking_time', 'servings', 'status', 'featured_image']


class SearchForm(forms.Form):
    """
    Form class for users to search on the website
    """
    query = forms.CharField(label='Search', max_length=100, validators=[MaxLengthValidator(100)])
