# Generated by Django 4.0 on 2022-01-09 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('TUFIDCOapp', '0059_schemesanctionpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencysanctionform',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
        ),
    ]
