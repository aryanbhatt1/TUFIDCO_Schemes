# Generated by Django 4.0.4 on 2022-05-20 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_monthwisereport'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorWiseReport',
            fields=[
            ],
            options={
                'verbose_name': 'Sector Wise Report',
                'verbose_name_plural': 'Sector Wise Report',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Accounts.releaserequestmodel',),
        ),
    ]
