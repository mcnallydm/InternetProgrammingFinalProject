# Generated by Django 4.0.3 on 2022-04-04 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_spell_area_shape_alter_spell_attack_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterclass',
            old_name='char_class',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='components',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='damagetype',
            old_name='damage_type',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='effect',
            old_name='effects',
            new_name='name',
        ),
    ]
