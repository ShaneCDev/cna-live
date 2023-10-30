from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=256)
    friendly_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    second_image = CloudinaryField('image', default='placeholder')
    third_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=256, unique=True, null=False)
    discount_applied = models.BooleanField(default=False)

    def __str__(self):
        return self.name
