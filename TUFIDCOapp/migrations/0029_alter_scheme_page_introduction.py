# Generated by Django 4.0 on 2022-01-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0028_scheme_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme_page',
            name='introduction',
            field=models.TextField(null=True),
        ),
    ]
