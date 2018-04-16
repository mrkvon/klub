# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-22 14:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0002_auto_20171109_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masscommunication',
            name='subject',
            field=models.CharField(help_text='Same variables as in template can be used', max_length=130, validators=[django.core.validators.RegexValidator('^((\\{\\w*\\|\\w*\\})?[^{}]*)*$', 'Gender strings must look like {male_variant|female_variant}'), django.core.validators.RegexValidator('^([^$]*(\\$(addressment|name|firstname|surname|street|city|zipcode|email|telephone|regular_amount|regular_frequency|var_symbol|last_payment_amount)\\b)?)*$', 'Unknown variable')], verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='masscommunication',
            name='subject_en',
            field=models.CharField(blank=True, help_text='English version of the subject. If empty, English speaking users will not receive this communication.<br/>Same variables as in template can be used', max_length=130, null=True, validators=[django.core.validators.RegexValidator('^((\\{\\w*\\|\\w*\\})?[^{}]*)*$', 'Gender strings must look like {male_variant|female_variant}'), django.core.validators.RegexValidator('^([^$]*(\\$(addressment|name|firstname|surname|street|city|zipcode|email|telephone|regular_amount|regular_frequency|var_symbol|last_payment_amount)\\b)?)*$', 'Unknown variable')], verbose_name='English subject'),
        ),
        migrations.AlterField(
            model_name='masscommunication',
            name='template',
            field=models.TextField(help_text='Template can contain following variable substitutions: <br/>{mr|mrs}, $addressment, $name, $firstname, $surname, $street, $city, $zipcode, $email, $telephone, $regular_amount, $regular_frequency, $var_symbol, $last_payment_amount', max_length=50000, null=True, validators=[django.core.validators.RegexValidator('^((\\{\\w*\\|\\w*\\})?[^{}]*)*$', 'Gender strings must look like {male_variant|female_variant}'), django.core.validators.RegexValidator('^([^$]*(\\$(addressment|name|firstname|surname|street|city|zipcode|email|telephone|regular_amount|regular_frequency|var_symbol|last_payment_amount)\\b)?)*$', 'Unknown variable')], verbose_name='Template'),
        ),
        migrations.AlterField(
            model_name='masscommunication',
            name='template_en',
            field=models.TextField(blank=True, help_text='Same variables as in template can be used', max_length=50000, null=True, validators=[django.core.validators.RegexValidator('^((\\{\\w*\\|\\w*\\})?[^{}]*)*$', 'Gender strings must look like {male_variant|female_variant}'), django.core.validators.RegexValidator('^([^$]*(\\$(addressment|name|firstname|surname|street|city|zipcode|email|telephone|regular_amount|regular_frequency|var_symbol|last_payment_amount)\\b)?)*$', 'Unknown variable')], verbose_name='English template'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='password'),
        ),
    ]