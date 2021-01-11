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

    def test_save_image(self):
        self.testInstance.saveImage()
        filterImage= Image.objects.all()
        self.assertTrue(len(filterImage) > 0)

    def test_delete_image(self):
        self.testInstance.deleteImage()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.testInstance.saveImage()
        self.testInstance.updateImage(self.testInstance.id, 'images/img.jpg')
        imgUpdt = Image.objects.filter(image='images/test.jpg')
        self.assertTrue(len(imgUpdt) > 0)

    def test_get_image_by_id(self):
        imageF = self.testInstance.getimageById(self.testInstance.id)
        image = Image.objects.filter(id=self.testInstance.id)
        self.assertTrue(imageF, image)
