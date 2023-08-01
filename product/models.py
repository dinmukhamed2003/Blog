from django.db import models
from django.contrib.auth.models import User

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

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}_{self.text}'