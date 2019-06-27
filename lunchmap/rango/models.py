from django.db import models
import sys
from django.contrib.auth.models import User
class Place(models.Model):
    address = models.CharField(max_length=sys.maxsize)
    google_id = models.CharField(max_length=sys.maxsize)
    information = models.CharField(max_length=sys.maxsize)
    phone_number = models.CharField(max_length=sys.maxsize)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

class Review(models.Model):
    place_id = models.CharField(max_length=sys.maxsize)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.CharField(max_length=sys.maxsize)

