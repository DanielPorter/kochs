# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0002_donation_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='title',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='institutiontype',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='primaryemployment',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='primaryemployment',
            name='salary',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='primaryemployment',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
