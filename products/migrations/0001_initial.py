# Generated by Django 4.0.2 on 2022-03-04 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='auctioned_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_bid_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('auction_end_dateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='product_info',
            fields=[
                ('product_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField(max_length=1200)),
                ('product_photo', models.ImageField(upload_to='product_img')),
            ],
        ),
        migrations.CreateModel(
            name='user_bidding',
            fields=[
                ('bid_id', models.AutoField(primary_key=True, serialize=False)),
                ('final_bid', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.auctioned_product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auctioned_product',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product_info'),
        ),
        migrations.AddField(
            model_name='auctioned_product',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
