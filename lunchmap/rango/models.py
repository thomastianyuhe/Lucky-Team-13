from django.db import models
import math
import sys
class Place(models.Model):
    address = models.CharField(max_length=sys.maxsize)
    google_id = models.CharField(max_length=sys.maxsize)
    information = models.CharField(max_length=sys.maxsize)
    phone_number = models.CharField(max_length=sys.maxsize)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

# class Review(models.Model):

