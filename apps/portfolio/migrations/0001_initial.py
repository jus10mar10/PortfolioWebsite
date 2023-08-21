# Generated by Django 4.2.4 on 2023-08-21 03:53

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField(max_length=140)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='thumbnails/')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField(max_length=140)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='thumbnails/')),
            ],
        ),
    ]
