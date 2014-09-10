from django.db import models
from django.utils.translation import ugettext_lazy as _


class Direccion(models.Model):
    TYPES_CHOICES = (
        ('CASA', u'Casa'),
    )

    type = models.CharField(_('Type'), max_length=20, choices = TYPES_CHOICES)

    departamento = models.CharField(_('Departement'), max_length = 50, blank = True)
    edificio     = models.CharField(_('Building'), max_length = 20, blank = True)
    piso         = models.CharField(_('Floor'), max_length = 20, blank = True)
    casa         = models.CharField(_('Door'), max_length = 20, blank = True)
    numero       = models.CharField(_('Number'), max_length = 30, blank = True)
    calle1       = models.CharField(_('Address 1'), max_length = 100, blank = True)
    calle2       = models.CharField(_('Address 2'), max_length = 100, blank = True)
    codigoPostal = models.CharField(_('ZIP code'), max_length = 5, blank = True)
    localidad    = models.CharField(_('City'), max_length = 100, blank = True)
    provincia    = models.CharField(_('State'), max_length = 100, blank = True)

    def __str__(self):
        return self.calle1 +' '+self.calle2+' '+self.provincia

class Nombre(models.Model):
    nombre       = models.CharField(_('Nombre'), max_length = 50, blank = True)
    apellido     = models.CharField(_('1er Apellido'), max_length = 20, blank = True)
    apellido2    = models.CharField(_('2do Apellido '), max_length = 20, blank = True)

    def __str__(self):
        return self.nombre +' '+self.apellido+' '+self.apellido2

class Menu(models.Model):
    nombre = models.CharField(max_length=255)
    costo  = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.nombre


class Centro(models.Model):
    nombre      = models.CharField(max_length=255)
    direccion   = models.ForeignKey(Direccion)
    codigo      = models.CharField(max_length = 255)
    expediente  = models.CharField(max_length = 255)
    email       = models.CharField(max_length = 255)
    telefono    = models.CharField(max_length = 255)
    personal    = models.CharField(max_length = 255)
    fax         = models.CharField(max_length = 255)
    def __str__(self):
        return self.nombre


class Tutor(models.Model):
   nombre      = models.ForeignKey(Nombre)
   direccion   = models.ForeignKey(Direccion)
   dni         = models.CharField(max_length = 255)
   email       = models.CharField(max_length = 255)
   telefono    = models.CharField(max_length = 255)
   telefonoAlt = models.CharField(max_length = 255)

   def __str__(self):
        return self.nombre


class Estudiante (models.Model):
    nombre      = models.ForeignKey(Nombre)
    dni         = models.CharField(max_length = 255)
    curso       = models.CharField(max_length = 255)
    dieta       = models.CharField(max_length = 255)
    nutricion   = models.CharField(max_length = 255)
    email       = models.CharField(max_length = 255)
    telefono    = models.CharField(max_length = 255)
    telefonoAlt = models.CharField(max_length = 255)
    etapa       = models.CharField(max_length = 255)
    direccion   = models.ForeignKey(Direccion)
    tutor       = models.ForeignKey(Tutor)
    centro      = models.ForeignKey(Centro)
    desayuno    = models.BooleanField(default = True)
    comida      = models.BooleanField(default = True)
    descuento   = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre


class Pago(models.Model):
    fechaHora  = models.DateTimeField('Fecha y hora del pago')
    monto      = models.DecimalField(max_digits=12, decimal_places=2)
    tutor      = models.ForeignKey(Tutor)
    estudiante = models.ForeignKey(Estudiante)

    def __str__(self):
        return self.fechaHora


class Asistio(models.Model):
    asistente = models.ForeignKey(Estudiante)
    fechaHora = models.DateTimeField('Fecha y hora de la asistencia')
    menu      = models.ForeignKey(Menu)
    
    def __str__(self):
        return self.asistente.nombre + " en Fecha " + self.fechaHora.strftime("%Y-%m-%d %H:%M") + " se sirvio " + self.menu.nombre
