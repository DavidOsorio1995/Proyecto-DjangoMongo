from django.db import models

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField(default=0)  # Campo de cantidad
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField(default=0)  # Campo de cantidad
    proveedor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.name
