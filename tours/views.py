from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def mainView(request):
    return render(request, 'index.html')


def tourView(request, id):
    return render(request, 'tour.html')


def departureView(request, departure):
    return render(request, 'departure.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, что-то пошло не так :(. Запрашиваемая страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('ХЬЮСТОН, у нас проблемы... с сервером :(')
