# Generated by Django 4.1.3 on 2023-04-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0014_order_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]