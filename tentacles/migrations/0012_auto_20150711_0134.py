# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0011_auto_20150711_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
