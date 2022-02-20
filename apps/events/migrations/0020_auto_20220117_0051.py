# Generated by Django 3.1.14 on 2022-01-16 23:51

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20211212_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime_from',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time from'),
        ),
        migrations.AlterField(
            model_name='event',
            name='diet',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('vegetarian', 'Vegetarian'), ('meat', 'Meat'), ('vegan', 'Vegan'), ('kosher', 'Kosher'), ('halal', 'Halal'), ('gluten_free', 'Gluten free')], max_length=46, verbose_name='Diet'),
        ),
        migrations.AlterField(
            model_name='event',
            name='grant',
            field=models.CharField(choices=[('No grant', 'No grant'), ('other', 'Other grant')], default='no_grant', max_length=128, verbose_name='Grant'),
        ),
        migrations.AlterField(
            model_name='event',
            name='program',
            field=models.CharField(blank=True, choices=[('-', '---')], default='', max_length=128, verbose_name='Program'),
        ),
    ]