# Generated by Django 4.0.3 on 2022-04-04 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0031_alter_spell_char_class_alter_spell_components_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='diy_spells', to=settings.AUTH_USER_MODEL),
        ),
    ]
