# Generated by Django 3.2 on 2021-05-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_auto_20210508_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistic',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
    ]
