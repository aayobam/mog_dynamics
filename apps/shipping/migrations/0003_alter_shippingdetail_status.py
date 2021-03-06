# Generated by Django 4.0.4 on 2022-06-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_alter_shippingdetail_picked_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetail',
            name='status',
            field=models.CharField(choices=[('Received', 'Received'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('uk Custom', 'shipment undergoing US customs routine inspection'), ('us custom', 'shipment undergoing UK customs routine inspection'), ('ca custom', 'shipment undergoing CA customs routine inspection'), ('enroute nigeria', 'Shipment is now in transit to Lagos, Nigeria')], max_length=100, null=True),
        ),
    ]
