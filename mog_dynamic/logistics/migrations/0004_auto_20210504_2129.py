# Generated by Django 3.2 on 2021-05-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0003_auto_20210504_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistic',
            name='receiver_phone_no',
            field=models.BigIntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='logistic',
            name='sender_phone_no',
            field=models.BigIntegerField(max_length=11),
        ),
    ]
