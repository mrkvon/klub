# Generated by Django 2.2.19 on 2021-04-15 09:39
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210226_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hours_worked',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Hours worked'),
        ),
        migrations.AddField(
            model_name='event',
            name='promoted_in_magazine',
            field=models.BooleanField(default=False, verbose_name='Promoted in the magazine'),
        ),
        migrations.AddField(
            model_name='event',
            name='vip_action',
            field=models.BooleanField(default=False, verbose_name='Vip action'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start date'),
        ),
        migrations.AddField(
            model_name='event',
            name='invitation_text_short',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Short Invitation text'),
        ),
        migrations.AlterField(
            model_name='event',
            name='web_url',
            field=models.URLField(blank=True, null=True, verbose_name='Url address of website'),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('abbreviated_name', models.CharField(max_length=30, verbose_name='Abbreviated name')),
            ],
            options={
                'verbose_name': 'Qualification',
                'verbose_name_plural': 'Qualifications',
            },
        ),
        migrations.AddField(
            model_name='organizationteam',
            name='qualification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Qualification', verbose_name='Qualification'),
        ),
    ]