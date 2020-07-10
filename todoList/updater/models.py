from django.db import models

# Create your models here.

class Item(models.Model):
    task = models.CharField(max_lenth=255)
    completed = models.BooleanField()
    date = models.DateField()
    def __str__(self):
        return self.task




