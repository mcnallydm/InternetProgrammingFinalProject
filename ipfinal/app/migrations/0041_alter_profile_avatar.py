# Generated by Django 4.0.3 on 2022-04-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_remove_spell_favorite_remove_spell_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='profile_images'),
        ),
    ]
