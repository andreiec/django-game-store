from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('games/', views.getGames),
    path('games/<str:pk>/', views.getGame),
]
