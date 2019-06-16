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

class ImageTestClass(TestCase):
    def setUp(self):
        #creating a new location and saving it 

        self.nairobi = Location(location_name='Nairobi')
        self.nairobi.save_location()

        # creating a new category and saving it 

        self.food = Category(category_name='Food')
        self.food.save_category()

        #creating a new imaage

        self.new_image = Image(image_name ='eat',image_description='eatingafrica',image_category=self.food,image_location=self.nairobi)
       

        #Testing instance for the image 

        def test_instance(self):
            self.assertTrue(isinstance(self.new_image,Image))

        # Testing the save method for the Image class
        def test_save_method(self):
            self.new_image.save_image()

