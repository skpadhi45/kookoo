# Generated by Django 4.1.3 on 2023-02-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0005_customerpin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlogup',
            name='pin',
            field=models.CharField(default='', max_length=10),
        ),
    ]
