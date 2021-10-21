from django.shortcuts import render
from django.http import HttpResponse

games = [ 
    {'name': "game1", 'price': 10.1},
    {'name': "game2", 'price': 120.24},
    {'name': "game3", 'price': 13.3},
    {'name': "game4", 'price': 11.1},
    {'name': "game5", 'price': 10},
]

def market(request):
    context = { 'games': games }

    return render(request, 'market/market.html', context)


def game(request, pk):
    gameObj = None

    for i in games:
        if i['name'] == pk:
            gameObj = i

    return render(request, 'market/game.html', { 'game': gameObj })