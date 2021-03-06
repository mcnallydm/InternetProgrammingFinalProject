# Generated by Django 4.0.3 on 2022-04-07 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created_spells',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
        migrations.AddField(
            model_name='spell',
            name='creator',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_spells', to='app.profile'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.BooleanField(default=False)),
                ('score', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('player', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='app.profile')),
                ('spell', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='app.spell')),
            ],
        ),
    ]
