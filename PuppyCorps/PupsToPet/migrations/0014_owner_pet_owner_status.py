# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PupsToPet', '0013_auto_20171029_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='pet_owner_status',
            field=models.BooleanField(default=False, help_text='Are you a dog owner?'),
        ),
    ]
