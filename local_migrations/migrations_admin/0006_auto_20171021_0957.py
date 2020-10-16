# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-21 09:57
from __future__ import unicode_literals

from django.db import migrations


def populate_userprofile(apps, schema_editor):
    LogEntry = apps.get_model("admin", "LogEntry")
    for log_entry in LogEntry.objects.all():
        if log_entry.user:
            log_entry.user_profile = log_entry.user.userprofile
        log_entry.save()


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0005_auto_20171021_0910'),
        ('aklub', '0046_auto_20171020_1510'),
    ]

    operations = [
        migrations.RunPython(populate_userprofile, migrations.RunPython.noop)
    ]