# Generated by Django 4.0.4 on 2022-06-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetail',
            name='picked_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]