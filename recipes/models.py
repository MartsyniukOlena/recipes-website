from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.


class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    content = models.TextField(default='', help_text='Ingredients and Instructions')
    cooking_time = models.PositiveIntegerField(help_text='Time in minutes', default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    servings = models.PositiveIntegerField(help_text='Number of servings', default=0)
    is_featured = models.BooleanField(default=False)
    favorites = models.ManyToManyField(User, related_name='favorite', blank=True, default=None)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`recipes.Recipe`.
    """
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
