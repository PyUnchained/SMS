# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20150124_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(to='office.Subject', null=True),
            preserve_default=True,
        ),
    ]
