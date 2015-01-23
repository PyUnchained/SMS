# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=1000)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('read_on', models.DateTimeField(null=True, blank=True)),
                ('replied_on', models.DateTimeField(null=True, blank=True)),
                ('forwarded_on', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_by', models.ManyToManyField(related_name=b'deleted_by_user', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('recepients', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('reply_to_message', models.ForeignKey(related_name=b'reply_to', blank=True, to='msg_box.Message', null=True)),
                ('sender', models.ForeignKey(related_name=b'+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
