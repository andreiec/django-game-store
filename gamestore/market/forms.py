from django.forms import ModelForm, widgets
from django import forms
from .models import Game


# Form for new Game
class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'featured_image', 'price', 'website_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    # Update styling of input
    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})