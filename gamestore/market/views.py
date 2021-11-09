from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('market')

    context = {'form': form}
    return render(request, 'market/game_form.html', context)


# Update game form
def updateGame(request, pk):
    game = Game.objects.get(id=pk)
    form = GameForm(instance=game)

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)

        if form.is_valid():
            form.save()
            return redirect('market')

    context = {'form': form}
    return render(request, 'market/game_form.html', context)


# Delete game confirm
def deleteGame(request, pk):
    game =  Game.objects.get(id=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('market')

    context = { 'object': game }
    return render(request, 'market/delete_template.html', context) 