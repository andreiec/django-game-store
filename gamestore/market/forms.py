from django.forms import ModelForm
from .models import Game


# Form for new Game
class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'featured_image', 'price', 'website_link', 'tags']