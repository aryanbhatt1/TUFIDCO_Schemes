# Generated by Django 4.0 on 2022-01-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0088_alter_agencysanctionmodel_ts_awarded'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencysanctionmodel',
            name='tr_awarded',
            field=models.CharField(choices=[('0', 'Yes'), ('0', 'No')], max_length=20, null=True, verbose_name='Tender Sanction Awarded'),
        ),
        migrations.AddField(
            model_name='agencysanctionmodel',
            name='wd_awarded',
            field=models.CharField(max_length=20, null=True, verbose_name='Work Done Awarded'),
        ),
    ]
