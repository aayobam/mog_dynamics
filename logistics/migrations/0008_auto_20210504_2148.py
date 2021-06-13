# Generated by Django 3.2 on 2021-05-04 20:48

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0007_auto_20210504_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistic',
            name='receiver_phone_no',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='logistic',
            name='sender_phone_no',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]