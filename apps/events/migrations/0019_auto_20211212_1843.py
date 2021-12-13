# Generated by Django 2.2.24 on 2021-12-12 17:43

from django.db import migrations, models
from datetime import datetime, timezone


def date_to_datetime(apps, schema_editor):
    event_model = apps.get_model('events', 'event')
    for event in event_model.objects.all():
        just_date = event.date_from
        if just_date:
            date_with_time = datetime(just_date.year, just_date.month, just_date.day, 10, 1, 1, 1, tzinfo=timezone.utc)

            event.datetime_from = date_with_time
            event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_remove_location_administrative_unit'),
    ]

    operations = [
        # New basic purpose
        migrations.AlterField(
            model_name='event',
            name='basic_purpose',
            field=models.CharField(choices=[('action', 'Action'), ('action-with-attendee-list', 'Action with attendee list'), ('petition', 'Petition'), ('camp', 'Camp'), ('opportunity', 'Opportunity'), ('campaign', 'Campaign')], default='action', max_length=128, verbose_name='Basic Purpose'),
        ),
        migrations.AddField(
            model_name='event',
            name='datetime_from',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date from'),
        ),
        # Copy date from "date_from" to "datetime_from" and add time
        migrations.RunPython(date_to_datetime),
    ]
