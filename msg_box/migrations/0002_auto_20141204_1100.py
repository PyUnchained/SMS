# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg_box', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='forwarded_on',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='read_on',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='replied_on',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
