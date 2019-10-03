from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    

