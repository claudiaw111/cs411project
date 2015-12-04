# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151204_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='groups',
            name='user_id',
            field=models.ForeignKey(to='app.Users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(default=b'noID', max_length=10, serialize=False, verbose_name=b'user_id', primary_key=True),
        ),
    ]
