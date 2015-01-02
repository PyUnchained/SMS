# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50)),
                ('official_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'campuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('code', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('start_date', models.DateField()),
                ('exam_date', models.DateField(null=True, blank=True)),
                ('min_students', models.PositiveSmallIntegerField(blank=True)),
                ('max_students', models.PositiveSmallIntegerField(blank=True)),
                ('schedule', models.FileField(upload_to=b'office/schedules/%m/', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('campus', models.ForeignKey(to='office.Campus')),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommonAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('page', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100, blank=True)),
                ('syllabus_code', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('duration', models.PositiveSmallIntegerField(help_text=b'Duration in weeks')),
                ('is_active', models.BooleanField(default=True)),
                ('campuses', models.ManyToManyField(to='office.Campus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percent_grade', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('value_grade', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('personid', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('system_id', models.CharField(default=uuid.uuid4, max_length=36, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(default=b'', max_length=100)),
                ('surname', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1, verbose_name=b'sex', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('date_of_birth', models.DateField(verbose_name=b'date of Birth')),
                ('national_id', models.CharField(unique=True, max_length=50, verbose_name=b'National ID/Passport No.')),
                ('pic', models.FileField(upload_to=b'office/profile_pics/%Y/', verbose_name=b'Profile Picture')),
                ('card_id', models.CharField(default=uuid.uuid4, max_length=36, verbose_name=b'Card ID')),
                ('account_id', models.CharField(max_length=20, verbose_name=b'Account ID')),
                ('is_active', models.BooleanField(default=True)),
                ('billing_address_street', models.CharField(max_length=50, verbose_name=b'Billing Address (Number/Street)')),
                ('billing_address_city', models.CharField(max_length=50, verbose_name=b'city')),
                ('billing_address_country', models.CharField(max_length=50, verbose_name=b'country')),
                ('homephone', models.CharField(max_length=20, verbose_name=b'home Phone')),
                ('preffered_cell', models.CharField(help_text=b'Your preferred cellphone number to use.', max_length=50, verbose_name=b'cellphone')),
                ('secondary_cell', models.CharField(help_text=b'Your secondary cellphone number.', max_length=50, verbose_name=b'cellphone', blank=True)),
                ('tertiary_cell', models.CharField(help_text=b'Your tertiary cellphone number.', max_length=50, verbose_name=b'cellphone', blank=True)),
                ('email2', models.EmailField(help_text=b'Your secondary e-mail.', max_length=50, verbose_name=b'Secondary Email', blank=True)),
                ('skype', models.CharField(max_length=50, verbose_name=b'skype Name', blank=True)),
                ('registration_date', models.DateField()),
                ('role', models.CharField(max_length=2, verbose_name=b'Role', choices=[(b'L', b'Lecturer'), (b'LA', b'Low Level Admin'), (b'HA', b'High Level Admin'), (b'FA', b'Full Admin')])),
                ('is_on_leave', models.BooleanField(default=False)),
                ('contract', models.FileField(upload_to=b'office/staff/contracts/%Y/', verbose_name=b'Contract File')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name_plural': 'staff',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('personid', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('system_id', models.CharField(default=uuid.uuid4, max_length=36, editable=False)),
                ('name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(default=b'', max_length=100)),
                ('surname', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1, verbose_name=b'sex', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('date_of_birth', models.DateField(verbose_name=b'date of Birth')),
                ('national_id', models.CharField(unique=True, max_length=50, verbose_name=b'National ID/Passport No.')),
                ('pic', models.FileField(upload_to=b'office/profile_pics/%Y/', verbose_name=b'Profile Picture')),
                ('card_id', models.CharField(default=uuid.uuid4, max_length=36, verbose_name=b'Card ID')),
                ('account_id', models.CharField(max_length=20, verbose_name=b'Account ID')),
                ('is_active', models.BooleanField(default=True)),
                ('billing_address_street', models.CharField(max_length=50, verbose_name=b'Billing Address (Number/Street)')),
                ('billing_address_city', models.CharField(max_length=50, verbose_name=b'city')),
                ('billing_address_country', models.CharField(max_length=50, verbose_name=b'country')),
                ('homephone', models.CharField(max_length=20, verbose_name=b'home Phone')),
                ('preffered_cell', models.CharField(help_text=b'Your preferred cellphone number to use.', max_length=50, verbose_name=b'cellphone')),
                ('secondary_cell', models.CharField(help_text=b'Your secondary cellphone number.', max_length=50, verbose_name=b'cellphone', blank=True)),
                ('tertiary_cell', models.CharField(help_text=b'Your tertiary cellphone number.', max_length=50, verbose_name=b'cellphone', blank=True)),
                ('email2', models.EmailField(help_text=b'Your secondary e-mail.', max_length=50, verbose_name=b'Secondary Email', blank=True)),
                ('skype', models.CharField(max_length=50, verbose_name=b'skype Name', blank=True)),
                ('registration_date', models.DateField()),
                ('is_overdue', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100, blank=True)),
                ('subject_code', models.CharField(max_length=50, verbose_name=b'Subject Code')),
                ('description', models.TextField(max_length=300, verbose_name=b'Description')),
                ('courses', models.ManyToManyField(to='office.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(to='office.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(to='office.Course'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='office.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(to='office.Staff'),
            preserve_default=True,
        ),
    ]
