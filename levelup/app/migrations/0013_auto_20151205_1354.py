# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20151204_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challenger', models.CharField(default=b'None', max_length=50, verbose_name=b'challenger')),
                ('challengee', models.CharField(default=b'None', max_length=50, verbose_name=b'challengee')),
                ('gerExp', models.PositiveIntegerField(default=0)),
                ('geeExp', models.PositiveIntegerField(default=0)),
                ('remain', models.PositiveIntegerField(default=7)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='group',
            field=models.CharField(default=b'None', max_length=255, verbose_name=b'group'),
        ),
    ]
