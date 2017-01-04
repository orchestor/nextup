# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='areaCodeMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaCode', models.IntegerField()),
                ('region', models.IntegerField()),
                ('state', models.CharField(max_length=255)),
                ('division', models.CharField(choices=[('NorthWestern', 'NorthWestern'), ('SouthWestern', 'SouthWestern'), ('NorthCentral', 'NorthCentral'), ('SouthCentral', 'SouthCentral'), ('NorthEastern', 'NorthEastern'), ('SouthEastern', 'SouthEastern')], max_length=255)),
            ],
        ),
    ]