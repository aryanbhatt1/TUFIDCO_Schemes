# Generated by Django 4.0.4 on 2022-05-19 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0171_remove_fundreleasedetails_mastersanctionform_and_more'),
        ('reports', '0012_delete_progressnotentered_delete_sanctionnotentered_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
            ],
            options={
                'verbose_name': 'GO Wise Report',
                'verbose_name_plural': 'GO Wise Reports',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('TUFIDCOapp.mastersanctionform',),
        ),
        migrations.CreateModel(
            name='SectorMasterReport',
            fields=[
            ],
            options={
                'verbose_name': 'Sector wise Report',
                'verbose_name_plural': 'Sector wise Reports',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('TUFIDCOapp.mastersanctionform',),
        ),
    ]
