# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migration', '0007_auto_20160331_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend', to='migration.Person')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='migration.Person')),
            ],
        ),
    ]
