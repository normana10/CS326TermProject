# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupapp', '0002_auto_20171024_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(help_text="owner's email adress", max_length=254, null=True),
        ),
    ]
