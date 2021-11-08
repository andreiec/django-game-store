from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

from django.db.models.deletion import CASCADE
# Create your models here.

# Company Model
class Company(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    #logo = models.ImageField()
    website = models.CharField(max_length=1024)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


# Game Model
class Game(models.Model):
    #company_id = models.ForeignKey(Company, on_delete=CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    website_link = models.CharField(max_length=2048, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    review_count = models.IntegerField(default=0, null=True, blank=True)
    review_ratio = models.IntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Display title
    def __str__(self):
        return self.title


# Review Model
class Review(models.Model):
    #user_id
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    review_message = models.CharField(max_length=2048)
    review_score = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Display title
    def __str__(self):
        return self.title


# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=64)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Display name
    def __str__(self):
        return self.name