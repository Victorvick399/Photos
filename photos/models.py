from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Photos(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location, blank=True, null=True, default=0 ,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,  blank=True, null=True, default=0,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        category = Category.objects.filter(name__icontains=search_term)
        pic_results=cls.objects.filter(category_id=category)
        return pic_results

    @classmethod
    def get_image_by_id(cls,id):
        image = Photos.objects.filter(id=id)
        return image

    @classmethod
    def filter_by_location(cls,location):
        loc=Location.objects.filter(name__icontains=location)
        p_results=cls.objects.filter(location_id=loc)
        return p_results

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
