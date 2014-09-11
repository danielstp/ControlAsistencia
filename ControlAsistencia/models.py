from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField

class Provincia(models.Model):
    nombre = models.CharField(_('Provincia'), max_length = 50, blank = True)
    def __str__(self):
        return self.nombre

class Direccion(models.Model):
#    TYPES_CHOICES = (
#        ('CASA', u'Casa'),
#    )

#    type = models.CharField(_('Type'), max_length=20, choices = TYPES_CHOICES)

    departamento = models.CharField(_('Departamento'), max_length = 50, blank = True)
    edificio     = models.CharField(_('Edificio'), max_length = 20, blank = True)
    piso         = models.CharField(_('Piso'), max_length = 20, blank = True)
    casa         = models.CharField(_('Casa'), max_length = 20, blank = True)
    numero       = models.CharField(_('Numero'), max_length = 30, blank = True)
    calle1       = models.CharField(_('Calle 1'), max_length = 100, blank = True)
    calle2       = models.CharField(_('Calle 2'), max_length = 100, blank = True)
    codigoPostal = models.CharField(_('Codigo Postal'), max_length = 5, blank = True)
    localidad    = models.CharField(_('Ciudad'), max_length = 100, blank = True)
    provincia    = models.ForeignKey(Provincia,'Provincia')

    def __str__(self):
        return self.calle1 +' '+self.calle2+' '+self.provincia

class Nombre(models.Model):
    nombre       = models.CharField(_('Nombre'), max_length = 150, blank = True)
    apellido     = models.CharField(_('1er Apellido'), max_length = 120, blank = True)
    apellido2    = models.CharField(_('2do Apellido '), max_length = 120, blank = True)

    def __str__(self):
        return self.nombre +' '+self.apellido+' '+self.apellido2

class Menu(models.Model):
    nombre = models.CharField(max_length=255)
    costo  = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.nombre

class Beca(models.Model):
    nombre = models.CharField(max_length=255)
    monto  = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre + ' ' + str(self.monto) + '€'
class Centro(models.Model):
    nombre              = models.CharField(max_length=255)
    direccion           = models.ForeignKey(Direccion)
    codigo              = models.CharField('Código',max_length = 255)
    lote                = models.CharField(max_length = 255)
    expediente          = models.CharField(max_length = 255)
    email               = models.EmailField('Correo Electronico',max_length = 255)
    emailDirector       = models.EmailField(max_length = 255)
    emailResponsable    = models.EmailField(max_length = 255)
    emailEncargado      = models.EmailField(max_length = 255)
    comunidadAutonoma   = models.CharField(max_length = 255)
    telefono            = models.CharField(max_length = 255)
    telefono2           = models.CharField(max_length = 255)
    telDirector         = models.CharField(max_length = 255)
    telEncargado        = models.CharField(max_length = 255)
    telResponsable      = models.CharField(max_length = 255)
    personal            = models.CharField(max_length = 255)
    director            = models.CharField(max_length = 255)
    responsable         = models.CharField(max_length = 255)
    encargado           = models.CharField(max_length = 255)
    fax                 = models.CharField(max_length = 255)
    precioComida        = models.DecimalField(max_digits=12, decimal_places=2)
    precioDesayuno      = models.DecimalField(max_digits=12, decimal_places=2)
    beca                = models.ManyToManyField(Beca,blank=True, null=True)
    montoBeca           = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre


class Tutor(models.Model):
   nombre      = models.CharField(_('Nombre'), max_length = 150, blank = True)
   apellido    = models.CharField(_('1er Apellido'), max_length = 120, blank = True)
   apellido2   = models.CharField(_('2do Apellido '), max_length = 120, blank = True)
   direccion   = models.ForeignKey(Direccion)
   dni         = models.CharField(max_length = 255)
   email       = models.CharField(max_length = 255)
   telefono    = models.CharField(max_length = 255)
   telefonoAlt = models.CharField(max_length = 255)
   sexo = models.CharField(_('2do Apellido '), max_length = 120, blank = True, choices=['Masculino','Femenino'])

   def __str__(self):
        return self.email

class Curso(models.Model):
   nombre = models.CharField(max_length = 255)
   nivel = models.IntegerField()
   def __str__(self):
       return self.nombre + ' ' + str(self.nivel)

class Estudiante (models.Model):
   nombre      = models.CharField(_('Nombre'), max_length = 150, blank = True)
   apellido    = models.CharField(_('1er Apellido'), max_length = 120, blank = True)
   apellido2   = models.CharField(_('2do Apellido '), max_length = 120, blank = True)
   dni          = models.CharField(max_length = 255)
   nacionalidad = models.CountryFlied()
   cuenta       = models.CharField(max_length = 255)
   curso        = models.ForeignKey(Curso)
   dieta        = models.CharField(max_length = 255)
   nutricion    = models.CharField(max_length = 255)
   email        = models.CharField(max_length = 255)
   telefono     = models.CharField(max_length = 255)
   telefonoAlt  = models.CharField(max_length = 255)
   etapa        = models.CharField(max_length = 255)
   direccion    = models.ForeignKey(Direccion)
   tutor        = models.ForeignKey(Tutor)
   centro       = models.ForeignKey(Centro)
   desayuno     = models.BooleanField(default = True)
   comida       = models.BooleanField(default = True)
   descuento    = models.DecimalField(max_digits = 12, decimal_places = 2 )
   nacimiento   = models.DateField('Fecha de nacimiento')
   beca         = models.ManyToManyField(Beca,blank=True, null=True)
   final        = models.DateField('Fecha de fin de beca')
   sexo = models.CharField(_('Sexo '), max_length = 120, blank = True, choices=['Masculino','Femenino'])
   formaPago = models.CharField(_('Forma de Pago'), max_length = 120, blank = True, choices=['Efectivo','Banco'])
   def __str__(self):
      return self.dni


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



class Becario(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    beca = models.ForeignKey(Beca)
    monto  = models.DecimalField(max_digits=12, decimal_places=2)
    final   = models.DateField('Fecha de fin de beca')
    def __str__(self):
        return self.nombre

class BecaCentro(models.Model):
    centro = models.ForeignKey(Centro)
    beca = models.ForeignKey(Beca)
    monto  = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.nombre