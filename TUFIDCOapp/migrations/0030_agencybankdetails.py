# Generated by Django 4.0 on 2022-01-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0029_alter_scheme_page_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyBankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameBeneficiary', models.CharField(max_length=100, null=True, verbose_name='Name of the Beneficiary')),
                ('nameBank', models.CharField(max_length=100, null=True, verbose_name='Name of the Bank')),
                ('branch', models.CharField(max_length=100, null=True, verbose_name='Branch')),
                ('accountNo', models.CharField(max_length=100, null=True, verbose_name='Account Number')),
                ('IFSCcode', models.CharField(max_length=20, null=True, verbose_name='IFSC Code')),
            ],
            options={
                'verbose_name': 'Agency Bank Detail',
                'verbose_name_plural': 'Agency Bank Details',
            },
        ),
    ]
