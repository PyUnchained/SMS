# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='personid',
            field=models.CharField(max_length=20, unique=True, serialize=False, primary_key=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='personid',
            field=models.CharField(max_length=20, unique=True, serialize=False, primary_key=True, blank=True),
        ),
    ]
