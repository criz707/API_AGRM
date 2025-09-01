from django.db import models
from usuario.models import Usuario
from mesa.models import Mesa



class EstadoReserva(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Estado de la reserva")
    def __str__(self):
        return self.nombre


# Create your models here.
class Reserva(models.Model):
    fecha_inicio = models.DateTimeField()

    fecha_final = models.DateTimeField()
    fecha = models.DateTimeField(help_text="Fecha del día de la reserva")
    estado = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE, related_name='reservas')
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='reservas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva {self.id} - {self.usuario.nombre} - {self.fecha.strftime('%Y-%m-%d')}"