# Generated by Django 4.2.8 on 2024-05-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="profile_logo_path",
            field=models.TextField(null=True),
        ),
    ]
