from django.urls import path
from . import views


urlpatterns = [
    path('', views.market, name='market'),
    path('game/<str:pk>/', views.game, name='game'),
    path('add-game/', views.addGame, name='add-game'),
]
