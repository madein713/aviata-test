# Generated by Django 3.2.5 on 2021-07-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_booking_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_token',
            field=models.CharField(max_length=2000),
        ),
    ]
