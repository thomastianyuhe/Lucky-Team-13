from django.db import models

class Place(models.Model):
    address = models.CharField()
    google_id = models.CharField()
    information = models.CharField()
    phone_number = models.CharField()
    rating = models.DecimalField(decimal_places=1)

class Review(models.Model):

