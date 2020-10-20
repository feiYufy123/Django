# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-10-19 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=64)),
                ('wen', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'info',
            },
        ),
    ]