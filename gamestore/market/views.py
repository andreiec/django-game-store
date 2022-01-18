from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Game, Tag
from .forms import GameForm
from .utils import searchGames, paginateGames

# Main page
def market(request):
    games, search_query = searchGames(request)
    custom_range, games = paginateGames(request, games, 6)

    context = { 'games': games, 'search_query': search_query, 'custom_range': custom_range }
    return render(request, 'market/market.html', context)


# Specific game
def game(request, pk):
    game = Game.objects.get(id=pk)
    return render(request, 'market/game.html', { 'game': game })


# Add new game form
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def deleteGame(request, pk):
    game =  Game.objects.get(id=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('market')

    context = { 'object': game }
    return render(request, 'delete_template.html', context) 