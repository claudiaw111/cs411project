# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151204_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(default=b'noID', max_length=10, verbose_name=b'user_id'),
        ),
    ]
