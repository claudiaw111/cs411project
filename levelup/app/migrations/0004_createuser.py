# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151125_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=50, verbose_name=b'email')),
                ('password', models.CharField(max_length=255, verbose_name=b'password')),
            ],
        ),
    ]
