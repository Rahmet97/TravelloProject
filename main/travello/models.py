from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='pics')
    desc = models.TextField()
    rating = models.IntegerField(default=1)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField()