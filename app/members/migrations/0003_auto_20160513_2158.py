# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-13 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20160513_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cellphone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='homephone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]