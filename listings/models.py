from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ads', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(default='DZD', max_length=6)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    wilaya = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

class AdImage(models.Model):
    ad = models.ForeignKey(Ad, related_name='images', on_delete=models.CASCADE)
    image = models.URLField()
    order = models.IntegerField(default=0)
