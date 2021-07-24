from datetime import datetime, timedelta, time

from booking.service.booking import check_flights, get_booking
from booking.service.selector import get_all_valid_bookings
from core.celery import app


@app.task()
def fetch_bookings_tasks():
    cities = {
        "ALA": "TSE",
        "TSE": "ALA",
        "MOW": "ALA",
        "ALA": "MOW",
        "CIT": "ALA",
        "ALA": "CIT",
        "TSE": "MOW",
        "MOW": "TSE",
        "TSE": "LED",
        "LED": "TSE"
    }

    today = datetime.now()
    for k, v in cities.items():
        get_booking(date_from=today, date_to=today + timedelta(days=30), fly_from=k, fly_to=v)


@app.task()
def check_flights_task():
    all_bookings = get_all_valid_bookings()
    flag = False
    while flag is False:
        check_flights(all_bookings)
        if all_bookings.filter(is_valid=True):
            continue

        if datetime.now().time == time(23, 30):
            break

        flag = True
