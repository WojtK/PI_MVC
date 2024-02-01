from django.db import models
from rest_framework import serializers


class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    kupiony = models.BooleanField(default=False)

    def __str__(self):
        return self.nazwa