# Generated by Django 2.2.7 on 2019-11-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0055_auto_20191114_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativeunit',
            name='from_email_address',
            field=models.EmailField(default='kp@auto-mat.cz', max_length=254),
        ),
        migrations.AddField(
            model_name='administrativeunit',
            name='from_email_str',
            field=models.CharField(default='Klub pratel Auto*Matu <kp@auto-mat.cz>', max_length=255, verbose_name='Name'),
        ),
    ]
