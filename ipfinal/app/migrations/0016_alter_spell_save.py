# Generated by Django 4.0.3 on 2022-04-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_spell_area_spell_favorite_spell_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='save',
            field=models.CharField(choices=[('D', 'Dexterity Save'), ('S', 'Strength Save'), ('C', 'Constitution Save'), ('I', 'Intelligence Save'), ('W', 'Wisdom Save'), ('H', 'Charisma Save'), ('N', 'None')], default='None', max_length=30),
        ),
    ]
