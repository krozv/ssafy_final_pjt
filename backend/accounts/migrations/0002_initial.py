# Generated by Django 4.2.8 on 2024-05-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_liked_movie',
            field=models.ManyToManyField(to='movie.movie'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
