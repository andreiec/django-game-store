from django.shortcuts import render
from django.http import HttpResponse


def market(request):
    return render(request, 'market/market.html')


def game(request, pk):
    return render(request, 'market/game.html')