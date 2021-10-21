from django.urls import path
from . import views


urlpatterns = [
    path('games/', views.games, name='games'),
    path('game/<str:pk>/', views.game, name='game'),
]
