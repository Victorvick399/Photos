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

    # # Testing search by category method
    def test_search_by_category(self):
        self.pain.save_photo()
        self.emotions.save_category()
        result = Photos.search_by_category('Pain')
        self.assertEqual(self.pain,result)

    def test_get_image_by_id(self):
        self.pain.save_photo()
        got_photos = Photos.get_image_by_id(1)
        self.assertTrue(len(got_photos) == 1)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Photos.objects.all().delete()

class LocationTestClass(TestCase):
    def setUp(self):
        self.emotions = Category(name="Pain")
        self.emotions.save()

        self.nairobi = Location(name="Nairobi")
        self.nairobi.save()

        self.pain = Photos(id=1, name='James', description="Life is pain", location=self.nairobi,category=self.emotions)

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    # Testing Save method
    def test_save_method(self):
        self.nairobi.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    # Testing delete method
    def test_delete_method(self):
        self.nairobi.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) < 1)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Photos.objects.all().delete()


class CategoryTestClass(TestCase):
    def setUp(self):
        self.emotions = Category(name="Pain")
        self.emotions.save()

        self.nairobi = Location(name="Nairobi")
        self.nairobi.save()

        self.pain = Photos(id=1, name='James', description="Life is pain", location=self.nairobi,category=self.emotions)

    def test_instance(self):
        self.assertTrue(isinstance(self.emotions, Category))

    # Testing Save method
    def test_save_method(self):
        self.emotions.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    # Testing delete method
    def test_delete_method(self):
        self.emotions.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) < 1)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Photos.objects.all().delete()