from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    model = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_category')
    color = models.CharField(max_length = 20, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)
    manufacture_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

