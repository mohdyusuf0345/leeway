from django.db import models


# Create your models here.

class Movie_Model(models.Model):
    rdate = models.DateField()
    movie_name = models.CharField(max_length=64)
    hero = models.CharField(max_length=64)
    heroine = models.CharField(max_length=64)
