# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import letter.models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0011_auto_20160211_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=100, validators=[letter.models.min_length_validator]),
        ),
    ]