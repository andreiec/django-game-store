# Generated by Django 4.0 on 2022-01-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_alter_game_options_rename_game_id_review_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
