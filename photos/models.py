from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Location(models.Model):
    locationName = models.CharField(max_length=30)

    def saveLocation(self):
        self.save()

    def deleteLocation(self):
        self.delete()

    @classmethod
    def updateLocation(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.locationName