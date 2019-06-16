from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class LocationTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.nairobi = Location(location_name = 'Nairobi')

    #Testing insatnce 

    def test_instance (self):
        self.assertTrue(isinstance(self.nairobi,Location))


    # Testing save method 
    def test_save_method(self):
        self.nairobi.save_location()


class CategoryTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.food = Category(category_name = 'Food')

    #Testing insatnce 

    def test_instance (self):
        self.assertTrue(isinstance(self.food,Category))


    # Testing save method 
    def test_save_method(self):
        self.food.save_category()

