# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20150129_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 2, 10, 8, 36, 21, 835661, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents'),
            preserve_default=True,
        ),
    ]
