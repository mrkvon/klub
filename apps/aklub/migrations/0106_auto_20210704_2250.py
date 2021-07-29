# Generated by Django 2.2.24 on 2021-07-04 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0105_auto_20210531_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativeunit',
            name='vice_president',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='au_vice_president', to='aklub.UserProfile', verbose_name='Vice president'),
        ),
        migrations.AddField(
            model_name='administrativeunit',
            name='vice_president_since',
            field=models.DateField(blank=True, null=True, verbose_name='Vice president since'),
        ),
    ]