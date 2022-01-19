from django.forms import ModelForm, widgets
from django import forms
from .models import Game, Review


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


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_score', 'title', 'review_message']

        labels = {
            'review_score': 'Rate the game',
            'title': 'Add a title',
            'review_message': 'Add a comment'
        }

    # Update styling of input
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})