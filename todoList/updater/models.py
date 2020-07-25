from django.db import models

# Create your models here.

class Item(models.Model):
    task = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    def __str__(self):
        return self.task



class Note(models.Model):
    note = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        len_note = len(self.note)
        if len_note > 10:
            return self.note[0:10]
        else:
            return self.note
    
