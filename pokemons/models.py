from django.db import models

# Create your models here.


class Pokemon(models.Model):

    number = models.IntegerField()
    name = models.CharField(max_length=65)
    picture = models.URLField()
    height = models.IntegerField()
    width = models.IntegerField()
