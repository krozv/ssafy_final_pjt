# Generated by Django 4.2.8 on 2024-05-20 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.IntegerField()),
                ('actor_name', models.CharField(max_length=100)),
                ('actor_original_name', models.CharField(max_length=100)),
                ('actor_popularity', models.IntegerField(null=True)),
                ('profile_logo_path', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_id', models.IntegerField()),
                ('director_name', models.CharField(max_length=100)),
                ('director_original_name', models.CharField(max_length=100)),
                ('director_popularity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.IntegerField()),
                ('genre_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer_id', models.IntegerField()),
                ('producer_name', models.CharField(max_length=100)),
                ('producer_original_name', models.CharField(max_length=100)),
                ('producer_popularity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_id', models.IntegerField()),
                ('provider_name', models.CharField(max_length=50)),
                ('provider_logo_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100)),
                ('video_key', models.CharField(max_length=100)),
                ('video_name', models.TextField()),
                ('video_site', models.CharField(max_length=50)),
                ('official', models.BooleanField()),
                ('video_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='movie.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('movie_id', models.IntegerField()),
                ('adult', models.BooleanField(null=True)),
                ('popularity', models.IntegerField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('Provider', models.ManyToManyField(to='movie.provider')),
                ('actors', models.ManyToManyField(to='movie.actor')),
                ('director', models.ManyToManyField(to='movie.director')),
                ('genres', models.ManyToManyField(to='movie.genre')),
                ('producer', models.ManyToManyField(to='movie.producer')),
                ('video', models.ManyToManyField(to='movie.video')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movie.movie'),
        ),
        migrations.CreateModel(
            name='Boxoffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.TextField()),
                ('rank', models.IntegerField()),
                ('name', models.TextField()),
                ('en_name', models.TextField(null=True)),
                ('code', models.IntegerField()),
                ('acc_aud', models.IntegerField()),
                ('movie', models.ManyToManyField(to='movie.movie')),
            ],
        ),
    ]
