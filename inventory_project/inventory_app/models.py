from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)  # Campo de cantidad
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)  # Campo de cantidad

    def __str__(self):
        return self.name
