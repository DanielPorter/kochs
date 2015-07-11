# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0004_auto_20150620_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='institution',
            field=models.ForeignKey(to='tentacles.Institution'),
        ),
    ]
