# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0015_auto_20150711_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchDiscipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('people', models.ManyToManyField(to='tentacles.Person')),
            ],
        ),
        migrations.AddField(
            model_name='institution',
            name='site',
            field=models.TextField(blank=True),
        ),
    ]
