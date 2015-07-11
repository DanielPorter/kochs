# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0007_auto_20150621_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.ForeignKey(to='tentacles.InstitutionType', null=True),
        ),
    ]
