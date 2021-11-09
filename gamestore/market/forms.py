from django.forms import ModelForm
from .models import Game


# Form for new Game
class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'price', 'website_link', 'tags']