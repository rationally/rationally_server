# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default=''),
        ),
    ]