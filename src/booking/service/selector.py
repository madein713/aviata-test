
from datetime import datetime, date, timedelta
from booking.models import Booking
from booking.utils import convert_date


def get_bookings_by_data(**kwargs):
    date_from = convert_date(kwargs.pop("date_from"))
    date_to = convert_date(kwargs.pop("date_to"))

    bookings = Booking.objects.filter(
        d_time__date__range=[date_from, date_to],
        is_valid=True,
        **kwargs
    ).order_by("price")

    return bookings


def get_all_valid_bookings():
    return Booking.objects.filter(
        d_time__date__range=[
            date.today(), date.today() + timedelta(days=30)
        ],
        is_valid=True
    )
