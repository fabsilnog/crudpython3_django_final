from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    unid = models.CharField(max_length=10)
    qtde = models.IntegerField()
    data = models.DateField()

# Create your models here.
