# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tentacles', '0013_auto_20150711_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='recipient_institution',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='institution',
        ),
        migrations.AddField(
            model_name='payment',
            name='donor',
            field=models.ForeignKey(related_name='donor', default=1, to='tentacles.Institution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.ForeignKey(blank=True, to='tentacles.PaymentType', null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='year',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='recipient',
            field=models.ForeignKey(related_name='recipient', to='tentacles.Institution'),
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
