# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0010_auto_20150701_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='affiliation',
            old_name='position',
            new_name='title',
        ),
        migrations.AddField(
            model_name='affiliation',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='affiliation_type',
            field=models.ForeignKey(to='tentacles.AffiliationType', null=True),
        ),
    ]
