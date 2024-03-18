from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='')
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="recipe_posts")
    excerpt = models.TextField(blank=True)
    ingredients = models.TextField(verbose_name='Ingredients')
    instructions = models.TextField(verbose_name='Instructions')    
    cooking_time = models.PositiveIntegerField(help_text='Time in minutes', default=0, verbose_name='Cooking Time')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')
    servings  = models.PositiveIntegerField(help_text='Number of servings', default=0, verbose_name='Servings')
    is_featured = models.BooleanField(default=False)
    favourites = models.ManyToManyField(User, related_name='favourite', blank=True, default=None)

    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"