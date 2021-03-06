# Generated by Django 4.0 on 2022-01-05 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0034_agencysanctionform'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencysanctionform',
            name='physicalProgress',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='physicalProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_progress', models.FileField(null=True, upload_to='physicalProgress/', verbose_name='Physical Process')),
                ('AgencySanctionForm', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TUFIDCOapp.agencysanctionform')),
            ],
        ),
    ]
