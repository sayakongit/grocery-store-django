from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products')
    stock = models.IntegerField(default=100)
    price = models.CharField(max_length=50)
    description = models.TextField()

    
    def __str__(self):
        return self.product_name



