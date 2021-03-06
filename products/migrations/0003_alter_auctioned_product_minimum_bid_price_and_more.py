# Generated by Django 4.0.2 on 2022-03-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_auctioned_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioned_product',
            name='minimum_bid_price',
            field=models.DecimalField(auto_created=True, decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product_info',
            name='product_id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
