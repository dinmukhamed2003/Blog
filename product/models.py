from django.db import models

# Create your models here.

class Category(models.Model):
    icon = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=64)

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 related_name="products")

