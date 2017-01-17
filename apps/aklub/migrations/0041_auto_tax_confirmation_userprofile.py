# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 13:26
from __future__ import unicode_literals

from django.db import migrations


def populate_userprofile(apps, schema_editor):
    TaxConfirmation = apps.get_model("aklub", "TaxConfirmation")
    for tax_confirmation in TaxConfirmation.objects.all():
        tax_confirmation.user_profile = tax_confirmation.user.userprofile
        tax_confirmation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0040_auto_20170117_1325'),
    ]

    operations = [
        migrations.RunPython(populate_userprofile)
    ]
