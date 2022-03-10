# Generated by Django 4.0.2 on 2022-02-21 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_product_info_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_info',
            name='auction_end_dateTime',
        ),
        migrations.RemoveField(
            model_name='product_info',
            name='minimum_bid_price',
        ),
        migrations.CreateModel(
            name='auctioned_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_bid_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('auction_end_dateTime', models.DateTimeField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.product_info')),
            ],
        ),
    ]