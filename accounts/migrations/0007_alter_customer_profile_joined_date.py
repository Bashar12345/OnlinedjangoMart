# Generated by Django 4.0.2 on 2022-02-21 19:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_delete_auctioned_product_delete_product_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='joined_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
