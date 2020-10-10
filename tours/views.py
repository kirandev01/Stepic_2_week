from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from .data import *
import random




def main_view(request):
    random_tours = random.sample(list(tours.values()), 6)
    return render(request, 'index.html', {'random_tours': random_tours, 'title': title, 'subtitle': subtitle,
                                          'description': description, 'departures': departures})


def tour_view(request, id):
    tour = tours[id]
    return render(request, 'tour.html', {'tour': tour})


def departure_view(request, departure):

    return render(request, 'departure.html', {'title': title, 'subtitle': subtitle,
                                          'description': description, 'departures': departures})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, что-то пошло не так :(. Запрашиваемая страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('ХЬЮСТОН, у нас проблемы... с сервером :(')
