# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migration', '0003_auto_20160330_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduation_year', models.CharField(max_length=30)),
                ('surname', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migration.Class')),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='telephone_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='class_directory',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='migration.Person'),
        ),
    ]
