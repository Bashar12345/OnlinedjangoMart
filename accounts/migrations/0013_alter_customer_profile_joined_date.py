# Generated by Django 4.0.2 on 2022-02-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customer_profile_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='joined_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
