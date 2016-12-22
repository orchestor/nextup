# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userHandle', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1)),
                ('type', models.CharField(choices=[(b'A', b'Artist'), (b'L', b'Listener')], max_length=1)),
                ('areaCode', models.IntegerField()),
            ],
        ),
    ]
