# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0003_auto_20150620_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('salary', models.FloatField(default=0)),
                ('position', models.CharField(max_length=100)),
                ('primary', models.BooleanField(default=False)),
                ('institution', models.ForeignKey(to='tentacles.Person')),
                ('person', models.ForeignKey(related_name='person', to='tentacles.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_a', models.ForeignKey(related_name='person_a', to='tentacles.Person')),
                ('person_b', models.ForeignKey(related_name='person_b', to='tentacles.Person')),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='primaryemployment',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='primaryemployment',
            name='person',
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(related_name='donor', to='tentacles.Institution'),
        ),
        migrations.DeleteModel(
            name='PrimaryEmployment',
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_type',
            field=models.ForeignKey(to='tentacles.RelationshipTypes'),
        ),
    ]
