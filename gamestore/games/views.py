from django.shortcuts import render
from django.http import HttpResponse


def games(request):
    return HttpResponse("<h1>Jocuri</h1>")

def game(request, pk):
    return HttpResponse("<h1>aici e doar un joc</h1>" + pk)