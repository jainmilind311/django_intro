from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=20)

    def __str__(self):
        return self.topic_name
    

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    last_access = models.DateField()

    def __str__(self):
        return str(self.last_access)
    