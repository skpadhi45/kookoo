# Generated by Django 4.1.3 on 2023-02-04 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0008_alter_customerlogup_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogup',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kookooleShop.customerpin'),
        ),
    ]
