# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('institution', models.ForeignKey(to='tentacles.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryEmployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('salary', models.FloatField()),
                ('position', models.CharField(max_length=100)),
                ('institution', models.ForeignKey(to='tentacles.Person')),
                ('person', models.ForeignKey(related_name='person', to='tentacles.Person')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='recipient',
            field=models.ForeignKey(to='tentacles.Person'),
        ),
        migrations.AddField(
            model_name='paper',
            name='author',
            field=models.ForeignKey(related_name='primary_author', to='tentacles.Person'),
        ),
        migrations.AddField(
            model_name='paper',
            name='secondary_authors',
            field=models.ManyToManyField(to='tentacles.Person'),
        ),
        migrations.AddField(
            model_name='institution',
            name='type',
            field=models.ForeignKey(to='tentacles.InstitutionType'),
        ),
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(to='tentacles.Person'),
        ),
        migrations.AddField(
            model_name='donation',
            name='recipient_institution',
            field=models.ForeignKey(to='tentacles.Institution'),
        ),
    ]
