from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Club(models.Model):
    """
    Stores a single text about the club
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class EventForm(models.Model):
    """
    Stores a single attendance request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Event attendance form from {self.name}"
