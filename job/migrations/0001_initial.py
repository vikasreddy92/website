# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50)),
                ('appliedOn', models.DateField(help_text='Please use the following format: MM-DD-YYYY')),
                ('source', models.CharField(max_length=50)),
                ('jobId', models.CharField(blank=True, max_length=50)),
                ('jobDesc', models.CharField(blank=True, max_length=200)),
                ('statusLink', models.URLField(blank=True)),
                ('result', models.CharField(choices=[('A', 'accept'), ('R', 'reject'), ('U', 'unknown')], default='U', max_length=1)),
            ],
        ),
    ]