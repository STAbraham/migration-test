# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blahblah', models.CharField(max_length=235)),
                ('tatata', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asfasdf', models.CharField(default='', max_length=1)),
            ],
        ),
    ]
