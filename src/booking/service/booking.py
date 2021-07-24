from typing import List
import pytz
import logging
from datetime import datetime, date, timedelta
from requests.api import request
from requests.models import Response

from core.settings import KIWI_API, CHECK_FLIGHTS_API, PARTNER_ID

from booking.models import Booking


def create_booking(**kwargs) -> Booking:
    fly_from = kwargs.pop("flyFrom")
    fly_to = kwargs.pop("flyTo")
    id = kwargs.pop("id")
    d_time = datetime.utcfromtimestamp(kwargs.pop("dTime")).replace(tzinfo=pytz.timezone("UTC"))
    a_time = datetime.utcfromtimestamp(kwargs.pop("aTime")).replace(tzinfo=pytz.timezone("UTC"))
    price = kwargs.pop("price")
    booking_token = kwargs.pop("booking_token")

    return Booking.objects.create(
        id=id, fly_to=fly_to, fly_from=fly_from, d_time=d_time,
        a_time=a_time, price=price, booking_token=booking_token
    )


def get_booking(**kwargs) -> None:
    kwargs.update(partner=PARTNER_ID)
    try:
        response = make_request("GET", KIWI_API, params=kwargs)
    except Exception:
        return None

    date_month_advance = date.today() + timedelta(days=30)

    monthly_bookings = Booking.objects.filter(
        d_time__date__range=[
            date.today(), date_month_advance
        ]
    )

    bookings = response.json()["data"]

    for booking in bookings:
        try:
            monthly_bookings.get(id=booking["id"])
        except Booking.DoesNotExist:
            create_booking(**booking)


def check_flights(bookings: List[Booking]):
    params = {
        "v": 2,
        "bnum": 1,
        "pnum": 1,
        "currency": "KZT"
    }

    for booking in bookings:
        params.update(booking_token=booking.booking_token)
        try:
            response = make_request("GET", CHECK_FLIGHTS_API, params=params, timeout=30)
        except ValueError as e:
            logging.error(e)
            continue

        data = response.json()
        flights_checked = data.get('flights_checked')
        price_change = data.get("price_change")
        if flights_checked is False or price_change is True:
            if flights_checked is False:
                booking.is_valid = False
            if price_change is True:
                booking.price = data.get("conversion").get("amount")
            booking.save()


def make_request(method: str, url: str, **kwargs):
    headers = {
        "Content-Type": "application/json"
    }

    kwargs.update(headers=headers)
    result = request(method, url, **kwargs)

    return check_status(result)


def check_status(result: Response):
    if result.status_code == 200:
        return result
    else:
        raise ValueError
