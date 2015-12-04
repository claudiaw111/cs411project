# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151204_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(unique=True, max_length=255, verbose_name=b'group_name')),
                ('group_description', models.TextField()),
                ('creator', models.CharField(default=b'None', max_length=50, verbose_name=b'creator')),
                ('member_2', models.CharField(default=b'None', max_length=50, verbose_name=b'member_2')),
                ('member_3', models.CharField(default=b'None', max_length=50, verbose_name=b'member_3')),
            ],
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]
