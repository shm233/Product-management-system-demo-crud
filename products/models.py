from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    full_name = models.CharField(max_length=255, null=True)
    def __str__(self):
        return f"{self.username}"

class ProductModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    product_image = models.ImageField(upload_to='media/products', null=True)
    production_date = models.DateField(null=True)
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        related_name = 'Product'
        )
    def __str__(self):
        return f"{self.name}---{self.price}"
