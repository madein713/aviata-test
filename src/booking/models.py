from django.db import models


class Booking(models.Model):
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    id = models.CharField(max_length=255, primary_key=True)
    fly_from = models.CharField(max_length=255)
    fly_to = models.CharField(max_length=255)
    d_time = models.DateTimeField()
    a_time = models.DateTimeField()
    booking_token = models.CharField(max_length=2000)
    is_valid = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
