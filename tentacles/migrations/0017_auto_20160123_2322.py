# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0016_auto_20151101_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
