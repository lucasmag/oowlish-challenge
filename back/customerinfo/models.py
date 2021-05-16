from django.db import models

from customerinfo.utils import Gender


class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=Gender.choices())
    company = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    title = models.CharField(max_length=150, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)
