# Generated by Django 3.0.6 on 2020-08-18 02:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_storemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='completion_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='storemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/stores/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='storemodel',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]