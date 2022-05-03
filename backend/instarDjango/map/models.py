from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Body(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    imageUrl = models.URLField(max_length=200, default="https://cdn.discordapp.com/attachments/432564281113051136/952994827543404574/1355328252_2.gif")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    def __str__(self):
        return self.name
    def to_json(self):
        return {
            'name': self.name,
            'imageUrl': self.imageUrl,
            'parent': self.parent,
        }
