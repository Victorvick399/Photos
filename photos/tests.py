from django.test import TestCase
from .models import Photos, Category, Location
import datetime as dt

# Create your tests here.


class PhotosTestClass(TestCase):
    # set up method
    def setUp(self):
        self.emotions = Category(name="Pain")
        self.emotions.save()

        self.nairobi = Location(name="Nairobi")
        self.nairobi.save()

        self.pain = Photos(id=1, name='James', description="Life is pain", location=self.nairobi,category=self.emotions)

    def test_instance(self):
        self.assertTrue(isinstance(self.pain, Photos))

    # Testing Save method
    def test_save_method(self):
        self.pain.save_photo()
        photos = Photos.objects.all()
        self.assertTrue(len(photos) > 0)

    # Testing delete method
    def test_delete_method(self):
        self.pain.delete_photo()
        photos = Photos.objects.all()
        self.assertTrue(len(photos) < 1)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Photos.objects.all().delete()