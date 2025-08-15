from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime
# Create your tests here.
class MenuModelTest(TestCase):
    def test_str_representation(self):
        item = Menu.objects.create(title="Pasta", price=12.50, inventory=5)
        self.assertEqual(str(item), "Pasta : 12.50")


class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=datetime(2025, 8, 15, 19, 0)
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 4)