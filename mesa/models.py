from django.db import models

class Mesa(models.Model):
    numero = models.CharField(max_length=45)
    piso = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Mesa {self.numero} - Piso {self.piso}"