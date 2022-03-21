from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateField()
    description = models.CharField(max_length=3000)
    def __str__(self):
        return self.name