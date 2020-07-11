from django.db import models

# Create your models here.

class Item(models.Model):
    task = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    def __str__(self):
        return self.task




