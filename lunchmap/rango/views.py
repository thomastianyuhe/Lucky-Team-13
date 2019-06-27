from django.shortcuts import render
from .models import *

def main(request):
    response = {}
    return render(request, 'rango/main.html', response)

def placePut(request):
    resp = {}
    if request.method == 'POST':
        place = request.POST
        placeinstance = Place(googleid= place.get("id"), address= place.get("adress"),
                              information= place.get("information"), phone_number= place.get("phone_number"),
                              rating= place.get("rating"))
        placeinstance.save()
        print("Created: " + str(placeinstance))
    return render(request, 'rango/main.html', resp)
