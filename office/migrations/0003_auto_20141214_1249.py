# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_auto_20141127_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='books',
            field=models.CharField(default=b'IE', max_length=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='books',
            field=models.CharField(default=b'IE', max_length=6),
            preserve_default=True,
        ),
    ]
