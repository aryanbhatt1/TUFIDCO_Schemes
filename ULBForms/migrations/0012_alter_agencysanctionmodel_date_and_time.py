# Generated by Django 4.0.3 on 2022-03-22 08:24

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('ULBForms', '0011_alter_agencyprogressmodel_expenditure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencysanctionmodel',
            name='date_and_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, null=True),
        ),
    ]
