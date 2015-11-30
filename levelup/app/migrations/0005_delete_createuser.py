# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_createuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreateUser',
        ),
    ]
