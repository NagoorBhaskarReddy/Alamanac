# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0016_auto_20171008_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendances',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kids.Student'),
        ),
    ]