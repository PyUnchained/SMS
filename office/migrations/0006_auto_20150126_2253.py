# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_campus_is_active'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together=set([('title', 'subtitle'), ('title', 'subject_code')]),
        ),
    ]
