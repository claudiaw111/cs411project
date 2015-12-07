# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.CharField(default=b'noID', max_length=10, verbose_name=b'user_id')),
                ('user_strength', models.PositiveIntegerField(default=b'0')),
                ('user_agility', models.PositiveIntegerField(default=b'0')),
                ('user_willpower', models.PositiveIntegerField(default=b'0')),
                ('user_constitution', models.PositiveIntegerField(default=b'0')),
                ('user_achievement', models.BinaryField(default=b'00000000')),
                ('group', models.CharField(default=b'None', max_length=255, verbose_name=b'group')),
            ],
        ),
    ]
