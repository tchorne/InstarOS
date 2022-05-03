from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Event(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    time = models.DateField()
    description = models.CharField(max_length=3000)
    def __str__(self):
        return self.name
