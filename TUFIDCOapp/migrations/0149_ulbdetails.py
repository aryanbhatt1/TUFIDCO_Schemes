# Generated by Django 4.0.3 on 2022-03-18 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0148_alter_agencyprogressmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ULBDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulbName', models.CharField(help_text='As Per the Record', max_length=100, null=True, verbose_name='Name of the ULB')),
                ('regional_office_zone', models.CharField(max_length=100, null=True, verbose_name='Regional Office/Zone')),
                ('office_phone_number', models.CharField(max_length=100, null=True, verbose_name='Office Phone Number')),
                ('mail_id', models.EmailField(max_length=100, null=True, verbose_name='Email ID')),
                ('alternative_mail', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Alternative Email ID')),
                ('officials', models.CharField(max_length=100, null=True, verbose_name='Officials')),
                ('executive_commissionar_ph_no', models.CharField(max_length=100, null=True, verbose_name='Executive/Commissionar Phone No.')),
                ('me_je', models.CharField(max_length=100, null=True, verbose_name='Master Engineer/Junior Engineer')),
                ('administrative_district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TUFIDCOapp.district')),
                ('ulbtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TUFIDCOapp.agencytype', verbose_name='ULB Type')),
            ],
        ),
    ]
