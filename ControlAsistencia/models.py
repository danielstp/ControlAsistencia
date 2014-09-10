from django.db import models

class Menu(models.Model):
    nombre = models.CharField(max_length=255)
    costo  = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.nombre

class Centro(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class Tutor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    tutor = models.ForeignKey(Tutor)
    centro = models.ForeignKey(Centro)

    def __str__(self):
        return self.nombre

class Pago(models.Model):
    fechaHora = models.DateTimeField('Fecha y hora del pago')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    tutor = models.ForeignKey(Tutor)
    estudiante = models.ForeignKey(Estudiante)

    def __str__(self):
        return self.fechaHora

class Asistio(models.Model):
    asistente = models.ForeignKey(Estudiante)
    fechaHora = models.DateTimeField('Fecha y hora de la asistencia')
    menu = models.ForeignKey(Menu)
    
    def __str__(self):
        return self.asistente.nombre + " en Fecha " + self.fechaHora.strftime("%Y-%m-%d %H:%M") + " se sirvio " + self.menu.nombre

