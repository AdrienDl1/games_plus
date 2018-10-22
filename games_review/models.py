from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Type(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

class Game(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()
    types = models.ManyToManyField(Type)
# Create your models here.
