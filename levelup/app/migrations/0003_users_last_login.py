# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151206_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.PositiveIntegerField(default=b'0'),
        ),
    ]
