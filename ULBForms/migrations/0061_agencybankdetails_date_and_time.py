# Generated by Django 4.0.5 on 2022-06-11 08:56

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('ULBForms', '0060_remove_agencybankdetails_date_and_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencybankdetails',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, null=True),
        ),
    ]
