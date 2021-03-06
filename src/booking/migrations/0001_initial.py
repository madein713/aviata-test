# Generated by Django 3.2.5 on 2021-07-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=255)),
                ('fly_from', models.CharField(max_length=255)),
                ('fly_to', models.CharField(max_length=255)),
                ('d_time', models.DateTimeField()),
                ('a_time', models.DateTimeField()),
                ('booking_token', models.CharField(max_length=255)),
                ('is_valid', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
    ]
