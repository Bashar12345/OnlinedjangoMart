# Generated by Django 4.0.2 on 2022-03-12 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_auctioned_product_minimum_bid_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='product_description',
            field=models.TextField(max_length=2000),
        ),
    ]
