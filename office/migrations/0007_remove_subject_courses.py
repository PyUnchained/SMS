# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0006_auto_20150126_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='courses',
        ),
    ]
