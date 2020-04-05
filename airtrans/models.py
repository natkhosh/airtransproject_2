from django.db import models


class Booking(models.Model):

    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField()
    total_amount = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f'{self.book_ref}'


class Ticket(models.Model):

    ticket_no = models.PositiveIntegerField(primary_key=True)
    book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)
    passenger_id = models.CharField(max_length=50)
    passenger_name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100)

    # class Meta:
    #     unique_together = (('passenger_id', 'passenger_name'),)

    def __str__(self):
        return f'{self.ticket_no} - {self.book_ref} - {self.passenger_id} - {self.passenger_name}'


class Airport(models.Model):

    airport_code = models.CharField(max_length=4, primary_key=True)
    airport_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    coordinates = models.CharField(max_length=30)
    timezone = models.TextField(default='Europe/Moscow')

    def __str__(self):
        return f'{self.airport_code} - {self.airport_name} - {self.city}'


class Aircraft(models.Model):

    aircraft_code = models.CharField(max_length=3, default='', primary_key=True)
    model = models.CharField(max_length=30)
    range = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f'{self.aircraft_code} - {self.model}'


class Flight(models.Model):

    flight_id = models.PositiveIntegerField(primary_key=True)
    flight_no = models.CharField(max_length=10, null=True)
    scheduled_departure = models.DateTimeField(null=True)
    scheduled_arrival = models.DateTimeField(null=True)
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE, null=True)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=30, null=True)
    aircraft_code = models.ForeignKey(Aircraft, related_name='departure_airport', on_delete=models.CASCADE, null=True)
    actual_departure = models.DateTimeField(blank=True, null=True)
    actual_arrival = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (('flight_no', 'scheduled_departure'),)

    def __str__(self):
        return f'{self.flight_id} - {self.flight_no} - {self.departure_airport} - {self.arrival_airport} - {self.status}'


class TicketFlight(models.Model):

    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    fare_conditions = models.CharField(max_length=30, null=True)
    amount = models.PositiveIntegerField(verbose_name='ticket_price', null=False)

    def __str__(self):
        return f'{self.ticket_no} - {self.flight_id} - {self.fare_conditions} - {self.amount}'


class BoardingPass(models.Model):

    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    boarding_no = models.PositiveIntegerField(null=False)
    seat_no = models.CharField(max_length=5, null=True)

    # class Meta:
    #     unique_together = (('flight_id', 'seat_no'),)

    def __str__(self):
        return f'{self.ticket_no} - {self.flight_id} - {self.boarding_no} - {self.seat_no}'


class Seat(models.Model):

    aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True)
    seat_no = models.CharField(max_length=5, default='', primary_key=True)
    fare_conditions = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.aircraft_code} - {self.seat_no}'

