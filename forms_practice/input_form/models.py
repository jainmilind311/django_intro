from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    comments = models.CharField(max_length=400, blank=True)


