from django.db import models

# Create your models here.

class Productos(models.Model):

    nombreProd = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return f"{self.nombreProd} - ${self.precio}"
    
class Clientes(models.Model):

    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):

        return f"Apellido y Nombre: {self.apellido}, {self.nombre} - Email: {self.email}"
    
class Cursos(models.Model):

    curso = models.CharField(max_length=40)
    precio = models.IntegerField()
    turno = models.CharField(max_length=40)

    def __str__(self):

        return f"{self.curso} - Turno {self.turno} - ${self.precio}"

class Consultas(models.Model):

    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField()
    consulta = models.CharField(max_length=150)

    def __str__(self):

        return f"Consulta: {self.consulta} - Datos de contacto: {self.nombre} - {self.telefono} - {self.email}"