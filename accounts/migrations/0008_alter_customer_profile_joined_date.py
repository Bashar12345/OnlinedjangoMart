# Generated by Django 4.0.2 on 2022-02-21 19:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customer_profile_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 19, 34, 10, 299476, tzinfo=utc)),
        ),
    ]
