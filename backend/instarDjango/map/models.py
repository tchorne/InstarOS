from django.db import models

# Create your models here.
class Star(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.URLField(max_length=200, default="https://cdn.discordapp.com/attachments/432564281113051136/952994827543404574/1355328252_2.gif")
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
    imageUrl = models.URLField(max_length=200, default="https://cdn.discordapp.com/attachments/432564281113051136/952995078912241674/819133564.gif")
    def __str__(self):
        return self.name