# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PupsToPet', '0008_auto_20171029_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.ForeignKey(help_text='Host of event', null=True, on_delete=django.db.models.deletion.SET_NULL, to='PupsToPet.Owner'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pet',
            field=models.ManyToManyField(help_text='Pets attending event', to='PupsToPet.Pet'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.CharField(help_text="How old is your pet? Enter a number. (ex: '2', '10', or '15')", max_length=2, null=True),
        ),
    ]
