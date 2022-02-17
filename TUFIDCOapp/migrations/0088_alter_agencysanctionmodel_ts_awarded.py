# Generated by Django 4.0 on 2022-01-15 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0087_agencysanctionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencysanctionmodel',
            name='ts_awarded',
            field=models.CharField(choices=[('0', 'Yes'), ('0', 'No')], max_length=20, null=True, verbose_name='Technical Sanction Awarded'),
        ),
    ]
