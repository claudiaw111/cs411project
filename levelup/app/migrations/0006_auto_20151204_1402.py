# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_createuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_level',
        ),
        migrations.AddField(
            model_name='users',
            name='user_agility',
            field=models.PositiveIntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_constitution',
            field=models.PositiveIntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_strength',
            field=models.PositiveIntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_willpower',
            field=models.PositiveIntegerField(default=b'0'),
        ),
    ]
