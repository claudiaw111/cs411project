# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(default=b'00000000', max_length=50, verbose_name=b'oauth_token'),
        ),
        migrations.AddField(
            model_name='users',
            name='token_secret',
            field=models.CharField(default=b'00000000', max_length=50, verbose_name=b'oauth_token_secret'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_name',
            field=models.CharField(default=b'None', max_length=255, verbose_name=b'user_name'),
        ),
    ]
