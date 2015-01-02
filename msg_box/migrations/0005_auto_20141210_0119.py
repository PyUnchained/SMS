# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg_box', '0004_message_reply_to_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reply_to_message',
            field=models.ForeignKey(related_name=b'reply_to', blank=True, to='msg_box.Message', null=True),
        ),
    ]
