# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151204_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groups',
            name='user_id',
            field=models.ForeignKey(to='app.Users', to_field=b'user_id'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(default=b'noID', unique=True, max_length=10, verbose_name=b'user_id'),
        ),
    ]
