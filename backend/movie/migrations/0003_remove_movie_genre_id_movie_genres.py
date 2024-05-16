# Generated by Django 4.2.8 on 2024-05-16 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_genre_genre_id_genre_genre_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre_id',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movie.genre'),
        ),
    ]
