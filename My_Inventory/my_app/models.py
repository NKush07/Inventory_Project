from django.db import models

class Inventory(models.Model):
    product_name = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.product_name