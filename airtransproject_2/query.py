import django
import os
import sys
from django.urls import path
from django.contrib import admin
from django.conf import settings


#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airtransproject_2.settings')
django.setup()


#
# # this module
# me = os.path.splitext(os.path.split(__file__)[1])[0]
#
# # helper function to locate this dir
# def here(x):
#     return os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


# # SETTINGS
# DEBUG = True
# ROOT_URLCONF = me
# DATABASES = {"default": {}}  # required regardless of actual usage
#
#
# TEMPLATES = [
#     {"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": here(".")}
# ]

#
# STATIC_URL = "/static/"
# STATICFILES_DIRS = (here("static"),)


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]






if __name__ == "__main__":

    from airtrans.models import *

    # a. список рейсов между двумя аэропортами
    a_flight_no = Flight.objects.all().filter(departure_airport__airport_name="Domodedovo International Airport",
                                    arrival_airport__airport_name='Pulkovo International Airport')

    print('a. Список рейсов между двумя аэропортами:')
    for a in a_flight_no:
        print(a.flight_no)

    # b. список мест выбранного самолета
    b_seat_no = Seat.objects.all().filter(aircraft_code='CN1')    # b. Cessna208
    st = []
    for s in b_seat_no:
        st.append(s.seat_no)
    print('b. Список мест выбранного самолета: \n', *st)

    # с. список выданных посадочных талонов для выбранного перелета
    c_boarding_no = BoardingPass.objects.all().filter(flight_id='118')

    bn = []
    for b in c_boarding_no:
        bn.append(b.boarding_no)
    print('b. Список выданных посадочных талонов: \n', *bn)

    # d. список имен пассажиров данного рейса

    d_passenger_name = TicketFlight.objects.all().filter(flight_id='118')
    print('d. Список имен пассажиров данного рейса:')
    for p in d_passenger_name:
        print(p.ticket_no.passenger_name)




