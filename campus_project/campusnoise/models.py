from django.db import models


class Lugar(models.Model):
    TIPOS_ESPACIO = [
        ('Biblioteca', 'Biblioteca'),
        ('Cafeteria', 'Cafetería'),
        ('Sala', 'Sala de estudio'),
    ]

    nombre = models.CharField(max_length=100)
    edificio = models.CharField(max_length=100)
    tipo_espacio = models.CharField(max_length=50, choices=TIPOS_ESPACIO)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class ReporteRuido(models.Model):
    NIVELES_RUIDO = [
        ('Bajo', 'Bajo'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
    ]

    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    nivel_ruido = models.CharField(max_length=10, choices=NIVELES_RUIDO)
    ocupacion = models.IntegerField()
    wifi = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lugar.nombre} - {self.nivel_ruido}"
