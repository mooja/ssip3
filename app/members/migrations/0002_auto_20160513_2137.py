# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-13 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='member',
            name='zipcode',
        ),
    ]
