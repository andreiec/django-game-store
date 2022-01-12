from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from market.models import GameKey
from .models import Profile
from .forms import CustomUserCreationForm

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    owned_games = GameKey.objects.select_related().filter(user_id=pk)
    context = { 'profile': profile, 'game_keys': owned_games }
    return render(request, 'users/profile.html', context)


def loginUser(request):

    page = 'login'
    context = { 'page': page }
    
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Usernme does not exist!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or password is wrong!")

    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, "User logged out!")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User created!")

            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "An error has occured during registration!")

    context = { 'page': page, 'form': form }
    return render(request, 'users/login_register.html', context)