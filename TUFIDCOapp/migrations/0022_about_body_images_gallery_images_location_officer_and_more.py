# Generated by Django 4.0 on 2022-01-02 08:00

from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('TUFIDCOapp', '0021_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('about_text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='body_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_slider', models.FileField(blank=True, null=True, upload_to='')),
                ('reform_slider', models.FileField(blank=True, null=True, upload_to='')),
                ('photogallery_slider', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='gallery_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img', models.FileField(null=True, upload_to='gallery/')),
                ('place', models.CharField(max_length=40, null=True)),
                ('Date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
                ('location', mapbox_location_field.models.LocationField(map_attrs={'center': (80.243369, 13.0025217), 'cursor_style': 'pointer', 'fullscreen_button': True, 'geocoder': True, 'marker_color': 'Blue', 'navigation_buttons': True, 'readonly': True, 'rotate': True, 'style': 'mapbox://styles/mapbox/satellite-v9', 'track_location_button': True})),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('Designation', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme_Faq_Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=50, null=True, verbose_name='Number')),
                ('question', models.TextField(null=True)),
                ('answer', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tufidco_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='headerimages/')),
                ('title', models.TextField(blank=True, null=True)),
                ('govt_title', models.TextField(blank=True, null=True)),
                ('india_flag', models.ImageField(null=True, upload_to='headerimages/')),
                ('tamilnadulogo', models.ImageField(null=True, upload_to='headerimages/')),
                ('Number', models.CharField(max_length=13, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('fax', models.TextField(blank=True, null=True)),
                ('webURL', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('TUFIDCOapp.mastersanctionform',),
        ),
        migrations.CreateModel(
            name='postreformslider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('reform_sliders', models.FileField(null=True, upload_to='reforms/')),
                ('reform_img', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TUFIDCOapp.body_images')),
            ],
        ),
        migrations.CreateModel(
            name='postphotogallery_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photogallery_sliders', models.FileField(null=True, upload_to='photogallery/')),
                ('body_img', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TUFIDCOapp.body_images')),
            ],
        ),
        migrations.CreateModel(
            name='postmainslider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainsliders', models.FileField(null=True, upload_to='photogallery/')),
                ('mainslider', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TUFIDCOapp.body_images')),
            ],
        ),
    ]
