from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()

class Cat(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
