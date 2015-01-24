# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_auto_20150124_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='subject',
            field=models.ManyToManyField(to='office.Subject', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='completionevent',
            name='for_subject',
            field=models.ForeignKey(to='office.Subject', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='classes',
            field=models.ManyToManyField(to=b'office.Class', null=True),
        ),
    ]
