from django.db import models

# Create your models here.
class Star(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.URLField(max_length=200)
    def __str__(self):
        return self.name
    def to_json(self):
        return {
            'name': self.name,
            'imageUrl': self.imageUrl,
        }

class Planet(models.Model):
    name = models.CharField(max_length=200)
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    imageUrl = models.URLField(max_length=200)
    def __str__(self):
        return self.name