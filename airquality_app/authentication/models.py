from django.db import models

class user(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
# Create your models here.
