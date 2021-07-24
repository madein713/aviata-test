from datetime import date, timedelta, datetime
from rest_framework import views, serializers, status
from rest_framework.response import Response
from booking.models import Booking
from booking.service.booking import get_booking

from booking.service.selector import get_bookings_by_data
from booking.utils import convert_date


class BookingAPI(views.APIView):

    class InputSerializer(serializers.Serializer):
        """
        date example 23/07/2021
        """
        fly_to = serializers.CharField(required=False)
        fly_from = serializers.CharField()
        date_from = serializers.CharField()
        date_to = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        class Meta:
            model = Booking
            fields = ("fly_from", "fly_to", "price", "d_time", "a_time",)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        date_month_advance = date.today() + timedelta(days=30)
        date_from = convert_date(data.get("date_from")).date()
        date_to = convert_date(data.get("date_to")).date()

        if date_from > date.today():
            return Response(data="Date is not valid", status=status.HTTP_400_BAD_REQUEST)

        if date_month_advance > date_to:
            date_from = data["date_from"]
            fly_from = data["fly_from"]
            fly_to = data["fly_to"]

            get_booking(date_from=date_from, date_to=date_to, fly_from=fly_from, fly_to=fly_to)

        bookings = get_bookings_by_data(**data)
        if bookings:
            return Response(
                self.OutputSerializer(bookings), status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
