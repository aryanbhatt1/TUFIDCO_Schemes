# Generated by Django 4.0 on 2022-01-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0027_remove_mastersanctionform_appraisedcostbytufidco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Scheme Name')),
                ('introduction', models.CharField(max_length=600, null=True, verbose_name='Introduction')),
            ],
        ),
    ]
