# Generated by Django 4.0.4 on 2022-05-31 10:49

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('ULBForms', '0052_remove_agencybankdetails_date_and_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencybankdetails',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, null=True),
        ),
    ]
