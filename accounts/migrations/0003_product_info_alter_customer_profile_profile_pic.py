# Generated by Django 4.0.2 on 2022-02-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customer_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_info',
            fields=[
                ('product_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=1200)),
                ('product_photo', models.ImageField(upload_to='product_photo')),
                ('minimum_bid_price', models.IntegerField()),
                ('auction_end_dateTime', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='profile_pic',
            field=models.ImageField(upload_to='accounts/profile_pics'),
        ),
    ]
