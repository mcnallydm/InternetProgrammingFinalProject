# Generated by Django 4.0.3 on 2022-04-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_spell_description_alter_spell_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='area_shape',
            field=models.CharField(choices=[('N', 'None'), ('R', 'Radius'), ('C', 'Cube'), ('S', 'Sphere'), ('Y', 'Cylinder')], default='None', max_length=20),
        ),
    ]