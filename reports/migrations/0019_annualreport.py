# Generated by Django 4.0.5 on 2022-06-23 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0175_delete_usermodel'),
        ('reports', '0018_delete_progressnotcommenced'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualReport',
            fields=[
            ],
            options={
                'verbose_name': 'Annual Progress Report',
                'verbose_name_plural': 'Annual Progress Report',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('TUFIDCOapp.mastersanctionform',),
        ),
    ]
