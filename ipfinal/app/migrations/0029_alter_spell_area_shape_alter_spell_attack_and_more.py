# Generated by Django 4.0.3 on 2022-04-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_spell_ritual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='area_shape',
            field=models.CharField(choices=[('None', 'None'), ('Radius', 'Radius'), ('Cube', 'Cube'), ('Sphere', 'Sphere'), ('Cylinder', 'Cylinder'), ('Cone', 'Cone')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='spell',
            name='attack',
            field=models.CharField(choices=[('None', 'None'), ('Melee', 'Melee Spell Attack'), ('Ranged', 'Ranged Spell Attack')], default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='spell',
            name='rating',
            field=models.IntegerField(blank=True, choices=[('No Rating', 'No Rating'), ('1/5', '1/5'), ('2/5', '2/5'), ('3/5', '3/5'), ('4/5', '4/5'), ('5/5', '5/5')], null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='saving_throw',
            field=models.CharField(choices=[('None', 'None'), ('Dexterity', 'Dexterity Save'), ('Strength', 'Strength Save'), ('Constitution', 'Constitution Save'), ('Intelligence', 'Intelligence Save'), ('Wisdom', 'Wisdom Save'), ('Charisma', 'Charisma Save')], default='None', max_length=30),
        ),
    ]