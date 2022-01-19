from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GameSerializer
from market.models import Game


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/games'},
        {'GET': 'api/games/id'},
        {'GET': 'api/games/id/review'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getGames(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getGame(request, pk):
    games = Game.objects.get(id=pk)
    serializer = GameSerializer(games, many=False)
    return Response(serializer.data)