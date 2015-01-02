# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('msg_box', '0002_auto_20141204_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='deleted_by',
            field=models.ManyToManyField(related_name=b'deleted_by_user', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
