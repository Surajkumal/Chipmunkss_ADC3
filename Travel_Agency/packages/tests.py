from django.test import TestCase

from .models import Packages

from datetime import datetime

# Create your tests here.
class PackageTest(TestCase):
	def setUp(self):
		Package.objects.create(title="Holiday",
			name="Sukute Beach", date=datetime.now()

			)


	def test_ORM(self):
		p = Package.objects.get(title="Holiday")
		self.assertEqual(p.title, "Holiday")	