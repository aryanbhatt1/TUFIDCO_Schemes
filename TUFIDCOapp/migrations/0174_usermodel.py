# Generated by Django 4.0.5 on 2022-06-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0173_remove_agencyname_pid_remove_district_pid'),
    ]

    operations = [
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(default='0', max_length=150)),
            ],
        ),
    ]
