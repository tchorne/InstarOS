from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Character(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Note(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=400)
    def __str__(self):
        return self.note_text
