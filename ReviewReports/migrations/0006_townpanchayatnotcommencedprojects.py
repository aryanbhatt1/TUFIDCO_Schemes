# Generated by Django 4.0.4 on 2022-05-26 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ULBForms', '0046_alter_agencyprogressmodel_nc_choices'),
        ('ReviewReports', '0005_municipalitynotcommencedprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='TownPanchayatNotCommencedProjects',
            fields=[
            ],
            options={
                'verbose_name': 'CTP Not Commenced Projects',
                'verbose_name_plural': 'CTP Not Commenced Projects',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ULBForms.agencyprogressmodel',),
        ),
    ]
