# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0009_auto_20150701_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='type',
            new_name='institution_type',
        ),
    ]
