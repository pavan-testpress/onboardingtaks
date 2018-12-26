from django.test import TestCase
from .models import Places
# Create your tests here.


class PlacesTestCases(TestCase):
    def setUp(self):
        Places.objects.create(
            title='Working Location',
            location=(78.98071289062497, 10.55262180194872),
            description='Working place',
            address='pallavaram',
            phone='8121710526',
            city='Chennai',
            type_of_city='City',
            tags=('work',)
        )

    def testListPage(self):
        pass
