# -*- coding: utf-8 -*-
from django.db                import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators   import RegexValidator
from django_countries.fields  import CountryField


class Provincia(models.Model):
    nombre = models.CharField(_(u'Provincia'), max_length=250)

    def __unicode__(self):
        return self.nombre


class ComunidadAutonoma(models.Model):
    nombre = models.CharField(_(u'Comunidad Autonoma'), max_length=250)

    def __unicode__(self):
        return self.nombre

class Direccion(models.Model):
    # TYPES_CHOICES = (
    #        (u'CASA', u'Casa'),
    #    )

    #    type = models.CharField(_(u'Type'), max_length=20, choices = ['M','F'])

    departamento = models.CharField(_(u'Departamento'), max_length=50, blank=True)
    edificio     = models.CharField(_(u'Edificio'), max_length=20, blank=True)
    piso   = models.CharField(_(u'Piso'), max_length=20, blank=True)
    casa   = models.CharField(_(u'Casa'), max_length=20, blank=True)
    numero = models.CharField(_(u'Numero'), max_length=30, blank=True)
    calle1 = models.CharField(_(u'Calle 1'), max_length=100, blank=True)
    calle2 = models.CharField(_(u'Calle 2'), max_length=100, blank=True)
    codigoPostal = models.CharField(_(u'Codigo Postal'), max_length=5, blank=True)
    ciudad    = models.CharField(_(u'Ciudad'), max_length=100, blank=True)
    provincia = models.ForeignKey(Provincia)
    comunidad = models.ForeignKey(ComunidadAutonoma,help_text=u'Comunidad Autonoma')
    pais      = CountryField(u'Pais')

    class Meta:
        verbose_name = _(u'Dirección')
        verbose_name_plural = _(u'Direcciones')

    def __unicode__(self):
        return self.calle1 + u' ' + self.calle2 + u' ' + self.provincia.nombre


class Telefono(models.Model):
    numero = models.DecimalField(max_digits=12, decimal_places=0)
    tipo = models.CharField(max_length=12,
                            choices=[(u'Movil', _(u'Movil')), (u'Oficina', _(u'Oficina')), (u'Casa', _(u'Casa')),
                                     (u'Fax', _(u'Fax')), ])

    def __unicode__(self):
        return self.tipo + u': ' + str(self.numero)


class Persona(models.Model):
    nombre    = models.CharField(_(u'nombre'), max_length=250, blank=True)
    apellido  = models.CharField(_(u'1er Apellido'), max_length=250, blank=True)
    apellido2 = models.CharField(_(u'2do Apellido '), max_length=250, blank=True)
    direccion = models.ForeignKey(Direccion)
    dni       = models.CharField(_(u'DNI'), help_text=_(u'documento nacional de identidad'), max_length=255)
    email     = models.EmailField(max_length=255)
    telefono  = models.ForeignKey(Telefono)
    sexo      = models.CharField(_(u'Sexo'), max_length=10, blank=True,
                    choices=[(u'Masculino', _(u'Masculino')), (u'Femenino', _(u'Femenino'))])
    nacionalidad = CountryField()
    foto=models.ImageField(_(u'Fotografia'),upload_to=u'fotos', blank=True)

    def __unicode__(self):
        return self.nombre + u' ' + self.apellido + u' ' + self.apellido2


class Contacto(Persona):
    def __unicode__(self):
        return self.nombre + u' ' + self.apellido + u' ' + self.apellido2


class EstudianteBase(Persona):
    def __unicode__(self):
        return self.nombre + u' ' + self.apellido + u' ' + self.apellido2


class TipoMenu(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = _(u'Tipo de Menu')
        verbose_name_plural = _(u'Tipos de Menus')

    def __unicode__(self):
        return self.nombre


class Menu(models.Model):
    nombre = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.ForeignKey(TipoMenu)

    def __unicode__(self):
        return self.nombre + u' ' + str(self.costo) + u'€'


class Banco(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255, blank=True)
    iban = models.CharField(max_length=255, blank=True)
    codigoOficina = models.CharField(_(u'Codigo Oficina'), max_length=255, blank=True)
    dc1 = models.CharField(max_length=255, blank=True)
    dc2 = models.CharField(max_length=255, blank=True)
    bic = models.CharField(max_length=255, blank=True)
    fp = models.CharField(max_length=255, blank=True)
    telefono = models.ForeignKey(Telefono)

    def __unicode__(self):
        return self.nombre


class CuentaBanco(models.Model):
    numero = models.CharField(max_length=255, validators=[
        RegexValidator(regex=r'^[A-Z0-9]{4}(\ [0-9]{4}){5}$', message=u'ES00 0000 0000 0000 0000 0000')])
    banco = models.ForeignKey(Banco)

    def __unicode__(self):
        return self.numero


class Beca(models.Model):
    nombre = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return self.nombre + u' ' + str(self.monto) + u'€'


class Centro(models.Model):
    nombre         = models.CharField(max_length=255)
    direccion      = models.ForeignKey(Direccion)
    codigo         = models.CharField(_(u'Código'), max_length=255)
    lote           = models.CharField(max_length=255)
    expediente     = models.CharField(max_length=255)
    email          = models.EmailField(_(u'Correo Electrónico'), max_length=255)
    director       = models.ForeignKey(Contacto, related_name=u"Director", help_text=u"director de centro")
    responsable    = models.ForeignKey(Contacto,related_name=u"Responsable", help_text=u"responsable de comedor")
    encargado      = models.ForeignKey(Contacto,related_name=u'Encargado', help_text=u"encargado del comedor")
    precioComida   = models.DecimalField(max_digits=12, decimal_places=2)
    precioDesayuno = models.DecimalField(max_digits=12, decimal_places=2)
    beca           = models.ManyToManyField(Beca, blank=True, null=True)
    montoBeca      = models.DecimalField(max_digits=12, decimal_places=2)
    telefono       = models.ForeignKey(Telefono)

    def __unicode__(self):
        return self.nombre


class Tutor(models.Model):
    persona = models.OneToOneField(Persona)
    class Meta:
        verbose_name = _(u'Tutor')
        verbose_name_plural = _(u'Tutores')

    def __unicode__(self):
        return self.persona.nombre + u' ' + self.persona.apellido

class Pagador(Tutor):
    cuenta = models.ForeignKey(CuentaBanco)

    class Meta:
       verbose_name_plural = _(u'Pagadores')
    def __unicode__(self):
        return self.persona.nombre + u' ' + self.persona.apellido + u' ' + self.persona.apellido2


class Etapa(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre 

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    etapa = models.ForeignKey(Etapa)
    nivel = models.IntegerField()

    def __unicode__(self):
        return self.nombre + u' ' + str(self.nivel)


class Estudiante(models.Model):
    persona    = models.ForeignKey(Persona)
    curso      = models.ForeignKey(Curso)
    dieta      = models.CharField(max_length=255, blank=True)
    nutricion  = models.CharField(max_length=255, blank=True)
    tutor      = models.ForeignKey(Tutor)
    centro     = models.ForeignKey(Centro)
    pagador    = models.ForeignKey(Pagador, related_name=u'pagador')
    nacimiento = models.DateField(u'Fecha de nacimiento')

    def __unicode__(self):
        return self.persona.nombre + u' ' + self.persona.apellido

class Documento(models.Model):
   nombre=models.CharField(_(u'nombre'), max_length=250)
   descripcion=models.CharField(_(u'descripcion'), max_length=250)
   fecha=models.DateTimeField(auto_now=True, editable=False)
   archivo=models.FileField(upload_to=u'documentos')
   persona=models.ForeignKey(Estudiante)
   def __unicode__(self):
     return self.nombre


class Pago(models.Model):
    fechaHora = models.DateTimeField(u'Fecha y hora del pago')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    tutor = models.ForeignKey(Pagador)
    estudiante = models.ForeignKey(Estudiante)
    formaPago = models.CharField(_(u'Forma de Pago'), max_length=120, blank=True,
                                 choices=[(u'Efectivo', u'Efectivo'), (u'Banco', u'Banco')])

    def __unicode__(self):
        return self.fechaHora


class Asistencia(models.Model):
    asistente = models.ForeignKey(Estudiante)
    fechaHora = models.DateTimeField(u'Fecha y hora de la asistencia')
    menu = models.ForeignKey(Menu)

    class Meta:
        verbose_name = _(u'Asistencia')
        verbose_name_plural = _(u'Asistencias')

    def __unicode__(self):
        return self.asistente.nombre + " en Fecha " + self.fechaHora.strftime(
            "%Y-%m-%d %H:%M") + " se sirvio " + self.menu.nombre + u' (' + self.menu.tipo.nombre + ')'


class Becado(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    beca = models.ForeignKey(Beca)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    final = models.DateField(u'Fecha de fin de beca')

    class Meta:
        verbose_name = _(u'Becado')
        verbose_name_plural = _(u'Becados')

    def __unicode___(self):
        return self.beca.beca


class BecaCentro(models.Model):
    centro = models.ForeignKey(Centro)
    beca = models.ForeignKey(Beca)
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return self.beca.nombre + u' ' + self.centro.nombre

class PlanAsistencia(models.Model):
    estudiante  = models.ForeignKey(Estudiante)
    tipoMenu    = models.OneToOneField(TipoMenu,primary_key=False)
    lunes       = models.BooleanField(default=False)
    martes      = models.BooleanField(default=False)
    miercoles   = models.BooleanField(default=False)
    jueves      = models.BooleanField(default=False)
    viernes     = models.BooleanField(default=False)
    sabado      = models.BooleanField(default=False)
    domingo     = models.BooleanField(default=False)
    fechaInicio = models.DateTimeField(auto_now=True,editable=False)
    def __unicode__(self):
        return "Lun "+str(self.lunes)+" ,Mar"+str(self.martes)+" ,Mie"+str(self.miercoles)+" ,Jue"+str(self.jueves)+" ,Vie"+str(self.viernes)+" ,Sab"+str(self.sabado)+" ,Dom"+str(self.domingo)
