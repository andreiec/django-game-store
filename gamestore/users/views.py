from django.shortcuts import render

from market.models import GameKey
from .models import Profile

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    owned_games = GameKey.objects.select_related().filter(user_id=pk)
    context = { 'profile': profile, 'game_keys': owned_games }
    return render(request, 'users/profile.html', context)
