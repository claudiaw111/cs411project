# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151204_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='user_id',
            field=models.CharField(default=b'noID', max_length=10, verbose_name=b'user_id'),
        ),
        migrations.AddField(
            model_name='groups',
            name='user_name',
            field=models.CharField(default=b'noName', max_length=255, verbose_name=b'user_name'),
        ),
    ]
