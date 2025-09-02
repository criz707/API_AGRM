from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Nombre del rol")


    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=45)

    correo = models.EmailField(max_length=45, unique=True)
    foto = models.TextField(max_length=150, null=True, blank=True)
    contrasena = models.CharField(max_length=50)
    
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return self.nombre
