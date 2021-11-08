from django.contrib import admin

# Register your models here.
from .models import Game, Review, Tag, Company

admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Company)