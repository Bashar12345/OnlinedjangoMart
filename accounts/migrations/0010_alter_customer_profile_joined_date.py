# Generated by Django 4.0.2 on 2022-02-22 05:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customer_profile_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 22, 5, 32, 22, 988959, tzinfo=utc)),
        ),
    ]
