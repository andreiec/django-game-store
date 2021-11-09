from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
from .forms import GameForm

# Main page
def market(request):
    games = Game.objects.all()
    context = { 'games': games }
    return render(request, 'market/market.html', context)


# Specific game
def game(request, pk):
    game = Game.objects.get(id=pk)
    return render(request, 'market/game.html', { 'game': game })


# Add new game form
def addGame(request):
    form = GameForm()
    context = {'form': form}
    return render(request, 'market/game_form.html', context)