from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Photos(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    location=models.ForeignKey(Location, blank=True, null=True, default=0)
    category=models.ForeignKey(Category,  blank=True, null=True, default=0)
    image=models.ImageField(upload_to='photos/')

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        pic_results = cls.objects.filter(category__icontains=search_term)
        return pic_results

    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name