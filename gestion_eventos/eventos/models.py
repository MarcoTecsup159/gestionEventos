from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos_organizados')

    def __str__(self):
        return self.nombre

class RegistroEvento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'evento')

    def __str__(self):
        return f'{self.usuario.username} registrado en {self.evento.nombre}'