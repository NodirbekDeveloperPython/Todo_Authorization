from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Plan(models.Model):
    nom = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=60, null=True)
    batafsil = models.TextField(blank=True)
    sana = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self): return self.nom