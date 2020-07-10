from django.db import models

# Create your models here.

class Customer(models.Model):
    nickname = models.CharField(max_length=10)
    fav_dish = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nickname
    
