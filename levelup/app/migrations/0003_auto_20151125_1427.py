# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151125_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=255, verbose_name=b'user_name'),
        ),
    ]
