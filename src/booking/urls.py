
from django.urls.conf import path
from booking.apis import BookingAPI


booking_patterns = [
    path("booking/", BookingAPI.as_view(), name="booking")
]
