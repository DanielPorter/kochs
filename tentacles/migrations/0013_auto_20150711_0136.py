# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0012_auto_20150711_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
