# Generated by Django 4.0.3 on 2022-04-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_spell_area_spell_area_shape_spell_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='saving_throw',
            field=models.CharField(choices=[('N', 'None'), ('D', 'Dexterity Save'), ('S', 'Strength Save'), ('C', 'Constitution Save'), ('I', 'Intelligence Save'), ('W', 'Wisdom Save'), ('H', 'Charisma Save')], default='None', max_length=30),
        ),
    ]
