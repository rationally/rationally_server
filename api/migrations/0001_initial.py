# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('PROPOSED', 'Proposed'), ('IN INVESTIGATION', 'In Investigation'), ('DECIDED', 'Decided'), ('DISCARDED', 'Discarded'), ('ON HOLD', 'On Hold')], default=('PROPOSED', 'Proposed'), max_length=20)),
                ('date_modified', models.DateTimeField(verbose_name='date modified')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
        ),
        migrations.AddField(
            model_name='alternative',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Topic'),
        ),
    ]
