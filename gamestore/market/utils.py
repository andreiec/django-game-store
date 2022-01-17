from .models import Tag, Game
from django.db.models import Q

def searchGames(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    games = Game.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(company__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return games, search_query