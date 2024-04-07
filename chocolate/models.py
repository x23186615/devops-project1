from django.db import models

class Chocolate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50)
    chocolate = models.ForeignKey(Chocolate, on_delete=models.CASCADE)

class Step(models.Model):
    description = models.TextField()
    chocolate = models.ForeignKey(Chocolate, on_delete=models.CASCADE)
