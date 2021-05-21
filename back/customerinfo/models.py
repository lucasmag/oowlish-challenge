from enum import Enum

from django.db import models


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class Gender(ChoiceEnum):
    MALE = "male"
    FEMALE = "female"


class City(models.Model):
    name = models.CharField(max_length=150, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=Gender.choices())
    company = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150, blank=True)
