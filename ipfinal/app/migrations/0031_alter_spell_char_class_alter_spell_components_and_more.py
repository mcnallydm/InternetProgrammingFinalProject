# Generated by Django 4.0.3 on 2022-04-04 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_rename_char_class_characterclass_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='char_class',
            field=models.ManyToManyField(blank=True, related_name='spell', to='app.characterclass'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='components',
            field=models.ManyToManyField(blank=True, related_name='spell', to='app.component'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='damage_type',
            field=models.ManyToManyField(blank=True, related_name='spell', to='app.damagetype'),
        ),
        migrations.AlterField(
            model_name='spell',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spell', to='app.school'),
        ),
    ]
