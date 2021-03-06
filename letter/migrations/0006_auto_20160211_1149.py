# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0005_letter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='address3',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='receiver_address2',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='receiver_address3',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='sender_contact',
        ),
        migrations.AddField(
            model_name='letter',
            name='receiver_name',
            field=models.CharField(blank=True, help_text='Receiver Name', max_length=100),
        ),
    ]
