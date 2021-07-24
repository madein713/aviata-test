from datetime import datetime


def convert_date(date: str):
    day, month, year = date.split("/")
    return datetime(year=int(year), month=int(month), day=int(day))
