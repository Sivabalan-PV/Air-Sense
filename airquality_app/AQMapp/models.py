from django.db import models

# Create your models here.
class EVChargingLocation(models.Model):
    station_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.station_name

class user(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
# Create your models here.