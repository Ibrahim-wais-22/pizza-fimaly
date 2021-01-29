from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField('price')
    
    def __str__(self):
        return str(self.name)
    
class Pie(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField('price')
    def __str__(self):
        return str(self.name)
    

class Juice(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField('price')
    
    def __str__(self):
        return str(self.name)

class Sandwich(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField('price')

    def __str__(self):
        return str(self.name)