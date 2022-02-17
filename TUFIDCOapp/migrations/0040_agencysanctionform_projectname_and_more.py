# Generated by Django 4.0 on 2022-01-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0039_remove_agencysanctionform_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencysanctionform',
            name='ProjectName',
            field=models.CharField(max_length=900, null=True, verbose_name='Project Name'),
        ),
        migrations.AlterField(
            model_name='agencysanctionform',
            name='physicalProgress',
            field=models.FileField(blank=True, help_text='Upload site photos indicating the Latitude and Longitude of the site, as generated by Google Maps', null=True, upload_to='', verbose_name='Physical Progress'),
        ),
    ]
