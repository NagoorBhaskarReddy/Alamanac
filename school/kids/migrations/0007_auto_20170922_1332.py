# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 13:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0006_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='t_mobile',
            new_name='t_subject',
        ),
    ]
