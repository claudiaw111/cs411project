# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151204_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=255, verbose_name=b'group_name')),
                ('group_description', models.TextField()),
                ('group_number', models.PositiveIntegerField(default=0, verbose_name=b'group_number')),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(default=b'noID', unique=True, max_length=10, verbose_name=b'user_id'),
        ),
        migrations.AddField(
            model_name='groups',
            name='user_id',
            field=models.ForeignKey(to='app.Users', to_field=b'user_id'),
        ),
    ]
