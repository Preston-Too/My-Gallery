from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(locationName='Nairobi')
        self.location.saveLocation()

        self.category = Category(categoryName='nature')
        self.category.saveCategory()

        self.testInstance = Image(id=1, imageName='IMG__001', imageDescription=' a test image', imageLocation=self.location,
                                imageCategory=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.testInstance, Image))
