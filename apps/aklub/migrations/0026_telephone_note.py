# Generated by Django 2.1.7 on 2019-03-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0025_auto_20190328_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='telephone',
            name='note',
            field=models.CharField(blank=True, help_text='e.g. do not call during a workweek', max_length=70, verbose_name='Note'),
        ),
    ]
