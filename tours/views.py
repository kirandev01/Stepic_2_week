from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError

import random

from .data import *






def main_view(request):
    random_tours = random.sample(list(tours.values()), 6)
    return render(request, 'index.html', {'random_tours': random_tours, 'title': title, 'subtitle': subtitle,
                                          'description': description, 'departures': departures})


def tour_view(request, id):
    departure = tours[id]['departure']
    letim_iz = departures[departure][3:]
    tour = tours[id]
    return render(request, 'tour.html', {'tour': tour, 'departures': departures, 'letim_iz': letim_iz})


def departure_view(request, departure):
    letim_iz = departures[departure][3:]
    dep_tours = {}
    n=0
    nights_from = 0
    nights_to = 0
    pricemin = 0
    pricemax = 0

    for id, tour in tours.items():
        if tour['departure'] == departure:
            tour2 = tour.copy()
            dep_tours[id] = tour2

            n = n + 1
            if nights_from == 0:
                nights_from = tour['nights']
            elif  nights_from > tour['nights']:
                nights_from = tour['nights']

            if nights_to == 0:
                nights_to = tour['nights']
            elif  nights_to < tour['nights']:
                nights_to = tour['nights']

            if pricemin == 0:
                pricemin = tour['price']
            elif  pricemin > tour['price']:
                pricemin = tour['price']

            if pricemax == 0:
                pricemax = tour['price']
            elif  pricemax < tour['price']:
                pricemax = tour['price']

    return render(request, 'departure.html', {'title': title, 'subtitle': subtitle,
                                          'description': description, 'departures': departures, 'letim_iz': letim_iz,
                                            'dep_tours': dep_tours, 'n': n, 'nights_from': nights_from,
                                            'nights_to': nights_to, 'pricemin': pricemin, 'pricemax': pricemax})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, что-то пошло не так :(. Запрашиваемая страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('ХЬЮСТОН, у нас проблемы... с сервером :(')
