# Generated by Django 4.0.4 on 2022-05-19 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0170_scrollmodel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundreleasedetails',
            name='masterSanctionForm',
        ),
        migrations.DeleteModel(
            name='CTPDistrictWiseReport',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='SectorMasterReport',
        ),
        migrations.DeleteModel(
            name='FundReleaseDetails',
        ),
    ]
