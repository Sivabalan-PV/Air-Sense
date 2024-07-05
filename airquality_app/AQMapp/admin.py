from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import user,EVChargingLocation

admin.site.register(user)
admin.site.register(EVChargingLocation)
