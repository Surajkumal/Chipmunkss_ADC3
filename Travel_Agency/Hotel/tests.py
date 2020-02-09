from django.test import TestCase
from Hotel.models import Hotel

class HotelTestCase(TestCase):
    def setup(self):
        Hotel.objects.create(destination="kathmandu" , Check_in="09/02/2020", Check_out="12/02/2020",children="0",Adults="2")

    def book_or_not(self):
        kathmandu = Hotel.objects.get(destination="kathmandu")
        self.assertEqual()