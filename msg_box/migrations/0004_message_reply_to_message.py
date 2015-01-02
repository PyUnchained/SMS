# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('msg_box', '0003_message_deleted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='reply_to_message',
            field=models.OneToOneField(related_name=b'reply_to', null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
