# Generated by Django 4.0.3 on 2022-03-29 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0151_delete_location'),
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardSingara',
            fields=[
            ],
            options={
                'verbose_name': 'Singara Chennai 2.0',
                'verbose_name_plural': 'Singara Chennai 2.0',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('TUFIDCOapp.mastersanctionform',),
        ),
        migrations.AlterModelOptions(
            name='dashboard',
            options={'verbose_name': 'KNMT', 'verbose_name_plural': 'KNMT'},
        ),
    ]
