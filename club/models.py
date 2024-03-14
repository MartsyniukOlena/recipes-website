from django.db import models

# Create your models here.

class Club(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    venue = models.TextField()
    agenda = models.TextField()
    datetime = models.DateTimeField(verbose_name="Date and Time")
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
