from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Resturant


def create(requeste):
    # Creacion de los Elementos 
    place = Place(name='Selva Negra', address='Colonia Tovar')
    place.save()

    #Creacion del Restaurante
    restaurant = Resturant(place=place, number_of_employees=10)

    restaurant.save()

    return HttpResponse(restaurant.place.name)

