# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migration', '0006_auto_20160331_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_catalog',
            name='university',
        ),
        migrations.DeleteModel(
            name='Course_Catalog',
        ),
    ]
