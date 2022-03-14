from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Note(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=400)
    def __str__(self):
        return self.note_text
