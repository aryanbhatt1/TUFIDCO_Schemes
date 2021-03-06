# Generated by Django 4.0.3 on 2022-03-22 08:29

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('ULBForms', '0012_alter_agencysanctionmodel_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencybankdetails',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='agencyprogressmodel',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='ulbpancard',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, null=True),
        ),
    ]
