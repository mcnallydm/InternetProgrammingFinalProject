# Generated by Django 4.0.3 on 2022-04-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_spell_upcasting_alter_spell_area_shape_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_class', models.ManyToManyField(blank=True, to='app.spell')),
            ],
        ),
    ]
