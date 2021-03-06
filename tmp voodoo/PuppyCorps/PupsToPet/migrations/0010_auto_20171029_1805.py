# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PupsToPet', '0009_auto_20171029_1754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['ID', 'start_time', 'end_time', 'location', 'host']},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='loc',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='startTime',
            new_name='start_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='pet',
        ),
        migrations.AddField(
            model_name='event',
            name='pet',
            field=models.ForeignKey(help_text="Owner's pet", null=True, on_delete=django.db.models.deletion.SET_NULL, to='PupsToPet.Pet'),
        ),
    ]
