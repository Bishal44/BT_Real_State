# Generated by Django 2.1.5 on 2019-02-21 11:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 21, 11, 32, 29, 701949, tzinfo=utc)),
        ),
    ]
