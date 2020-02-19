# Generated by Django 2.2.9 on 2020-02-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0006_auto_20200213_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interaction',
            name='text',
        ),
        migrations.RemoveField(
            model_name='interactiontype',
            name='text_bool',
        ),
        migrations.AddField(
            model_name='interactioncategory',
            name='display',
            field=models.BooleanField(default=True, help_text='Interactions under this category will show on timeline', max_length=130, verbose_name='Show on timeline'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='next_communication_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of next communication'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='status',
            field=models.CharField(blank=True, help_text='Status/progress of this communication', max_length=130, null=True, verbose_name='Status'),
        ),
    ]
