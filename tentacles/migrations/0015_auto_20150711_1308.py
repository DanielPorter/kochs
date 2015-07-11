# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0014_auto_20150711_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='country',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='parent',
            field=models.ForeignKey(related_name='inst_parent', blank=True, to='tentacles.Institution', null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='public_or_private',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='state',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
