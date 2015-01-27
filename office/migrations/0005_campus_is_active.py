# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_course_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
