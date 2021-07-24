from django.core.management.base import BaseCommand
from booking.service.booking import get_booking


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('date', type=str)

    def handle(self, *args, **options):
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
        for k, v in cities.items():
            get_booking(date_from=options["date"], fly_from=k, fly_to=v)
