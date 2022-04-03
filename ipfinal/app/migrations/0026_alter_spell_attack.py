# Generated by Django 4.0.3 on 2022-04-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_spell_area_shape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='attack',
            field=models.CharField(choices=[('N', 'None'), ('M', 'Melee Spell Attack'), ('R', 'Ranged Spell Attack')], default='None', max_length=30),
        ),
    ]