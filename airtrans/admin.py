from django.contrib import admin
from .models import *


admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(TicketFlight)
admin.site.register(BoardingPass)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Aircraft)
admin.site.register(Seat)

#
# from airtrans.models import *
#
#
# departure_airport__airport_code = "DME"
# Flight.objects.all().filter(departure_airport__airport_code=departure_airport__airport_code)
# # Register your models here.
