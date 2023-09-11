from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255) 
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    genre = models.CharField(max_length=30)
    date_added = models.DateField(auto_now_add=True)