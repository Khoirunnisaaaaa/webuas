from django.db import models

# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)