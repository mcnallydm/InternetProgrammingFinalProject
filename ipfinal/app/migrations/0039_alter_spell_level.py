# Generated by Django 4.0.3 on 2022-04-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_spell_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='level',
            field=models.IntegerField(help_text='Enter 0 for cantrips'),
        ),
    ]