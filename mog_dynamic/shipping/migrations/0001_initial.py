# Generated by Django 3.2 on 2021-05-03 19:10

from django.db import migrations, models
import shipping.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('items_description', models.TextField()),
                ('shipping_fee', models.BigIntegerField()),
                ('tracking_no', models.BigIntegerField(default=shipping.models.random_numbers)),
                ('received_date', models.DateTimeField(auto_now_add=True)),
                ('pending', models.BooleanField(default=False)),
                ('arrived', models.BooleanField(default=False)),
                ('picked_up', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('received_date',),
            },
        ),
    ]