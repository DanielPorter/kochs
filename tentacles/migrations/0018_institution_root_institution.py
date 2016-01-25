# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0017_auto_20160123_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='root_institution',
            field=models.ForeignKey(related_name='root_inst', blank=True, to='tentacles.Institution', null=True),
        ),
    ]
