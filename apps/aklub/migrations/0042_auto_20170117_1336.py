# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0041_auto_tax_confirmation_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxconfirmation',
            name='user',
        ),
    ]
