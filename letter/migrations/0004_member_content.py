# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_delete_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
