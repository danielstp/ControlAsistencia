from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class Provincia(models.Model):
    nombre = models.CharField(_('Provincia'), max_length=250)

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    # TYPES_CHOICES = (
    #        ('CASA', u'Casa'),
    #    )

    #    type = models.CharField(_('Type'), max_length=20, choices = ['M','F'])

    departamento = models.CharField(_('Departamento'), max_length=50, blank=True)
    edificio = models.CharField(_('Edificio'), max_length=20, blank=True)
    piso = models.CharField(_('Piso'), max_length=20, blank=True)
    casa = models.CharField(_('Casa'), max_length=20, blank=True)
    numero = models.CharField(_('Numero'), max_length=30, blank=True)
    calle1 = models.CharField(_('Calle 1'), max_length=100, blank=True)
    calle2 = models.CharField(_('Calle 2'), max_length=100, blank=True)
    codigoPostal = models.CharField(_('Codigo Postal'), max_length=5, blank=True)
    ciudad = models.CharField(_('Ciudad'), max_length=100, blank=True)
    provincia = models.ForeignKey(Provincia)
    comunidad = models.CharField(_('comunidad autonoma'),max_length=250)
    pais = CountryField('Pais')

    class Meta:
        verbose_name = _('Dirección')
        verbose_name_plural = _('Direcciones')

    def __str__(self):
        return self.calle1 + ' ' + self.calle2 + ' ' + self.provincia.nombre


class Telefono(models.Model):
    numero = models.DecimalField(max_digits=12, decimal_places=0)
    tipo = models.CharField(max_length=12,
                            choices=[('Movil', _('Movil')), ('Oficina', _('Oficina')), ('Casa', _('Casa')),
                                     ('Fax', _('Fax')), ])

    def __str__(self):
        return self.tipo + ': ' + str(self.numero)


class Persona(models.Model):
    nombre = models.CharField(_('nombre'), max_length=250, blank=True)
    apellido = models.CharField(_('1er Apellido'), max_length=250, blank=True)
    apellido2 = models.CharField(_('2do Apellido '), max_length=250, blank=True)
    direccion = models.ForeignKey(Direccion)
    dni = models.CharField(_('DNI'), help_text=_('documento nacional de identidad'), max_length=255)
    email = models.EmailField(max_length=255)
    telefono = models.ForeignKey(Telefono)
    sexo = models.CharField(_('Sexo'), max_length=10, blank=True,
                            choices=[('Masculino', _('Masculino')), ('Femenino', _('Femenino'))])
    nacionalidad = CountryField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.apellido2


class Contacto(Persona):
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.apellido2


class EstudianteBase(Persona):
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.apellido2


class TipoMenu(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Tipo de Menu')
        verbose_name_plural = _('Tipos de Menus')

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.ForeignKey(TipoMenu)

    def __str__(self):
        return self.nombre + ' ' + str(self.costo) + '€'


class Banco(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    iban = models.CharField(max_length=255)
    codigoOficina = models.CharField(_('Codigo Oficina'), max_length=255)
    dc1 = models.CharField(max_length=255)
    dc2 = models.CharField(max_length=255)
    bic = models.CharField(max_length=255)
    fp = models.CharField(max_length=255)
    telefono = models.ForeignKey(Telefono)

    def __str__(self):
        return self.nombre


class CuentaBanco(models.Model):
    numero = models.CharField(max_length=255, validators=[
        RegexValidator(regex=r'^[A-Z0-9]{4}(\ [0-9]{4}){5}$', message='ES00 0000 0000 0000 0000 0000')])
    banco = models.ForeignKey(Banco)

    def __str__(self):
        return self.numero


class Pagador(Persona):
    cuenta = models.ForeignKey(CuentaBanco)
    class Meta:
       verbose_name_plural = _('Pagadores')
    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' ' + self.apellido2


class Beca(models.Model):
    nombre = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre + ' ' + str(self.monto) + '€'


class Centro(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.ForeignKey(Direccion)
    codigo = models.CharField(_('Código'), max_length=255)
    lote = models.CharField(max_length=255)
    expediente = models.CharField(max_length=255)
    director = models.ForeignKey(Contacto, help_text="director de centro")
    responsable = models.ForeignKey(Contacto, help_text="director de centro")
    email = models.EmailField(_('Correo Electrónico'), max_length=255)
    comunidadAutonoma = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    responsable = models.CharField(max_length=255)
    encargado = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    precioComida = models.DecimalField(max_digits=12, decimal_places=2)
    precioDesayuno = models.DecimalField(max_digits=12, decimal_places=2)
    beca = models.ManyToManyField(Beca, blank=True, null=True)
    montoBeca = models.DecimalField(max_digits=12, decimal_places=2)
    telefono = models.ForeignKey(Telefono)

    def __str__(self):
        return self.nombre


class Tutor(models.Model):
    persona = models.OneToOneField(Persona)

    class Meta:
        verbose_name = _('Tutor')
        verbose_name_plural = _('Tutores')

    def __str__(self):
        return self.persona.nombre + ' ' + self.persona.apellido


class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + str(self.nivel)


class Estudiante(models.Model):
    nombre = models.OneToOneField(EstudianteBase)
    curso = models.ForeignKey(Curso)
    dieta = models.CharField(max_length=255)
    nutricion = models.CharField(max_length=255)
    etapa = models.CharField(max_length=255)
    tutor = models.ForeignKey(Tutor)
    pagador = models.ForeignKey(Pagador, related_name='pagador')
    centro = models.ForeignKey(Centro)
    nacimiento = models.DateField('Fecha de nacimiento')

    def __str__(self):
        return self.nombre.nombre + ' ' + self.nombre.apellido


class Pago(models.Model):
    fechaHora = models.DateTimeField('Fecha y hora del pago')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    tutor = models.ForeignKey(Pagador)
    estudiante = models.ForeignKey(Estudiante)
    formaPago = models.CharField(_('Forma de Pago'), max_length=120, blank=True,
                                 choices=[('Efectivo', 'Efectivo'), ('Banco', 'Banco')])

    def __str__(self):
        return self.fechaHora


class Asistencia(models.Model):
    asistente = models.ForeignKey(Estudiante)
    fechaHora = models.DateTimeField('Fecha y hora de la asistencia')
    menu = models.ForeignKey(Menu)

    class Meta:
        verbose_name = _('Asistencia')
        verbose_name_plural = _('Asistencias')

    def __str__(self):
        return self.asistente.nombre + " en Fecha " + self.fechaHora.strftime(
            "%Y-%m-%d %H:%M") + " se sirvio " + self.menu.nombre


class Becado(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    beca = models.ForeignKey(Beca)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    final = models.DateField('Fecha de fin de beca')

    class Meta:
        verbose_name = _('Becado')
        verbose_name_plural = _('Becados')

    def __str__(self):
        return self.nombre


class BecaCentro(models.Model):
    centro = models.ForeignKey(Centro)
    beca = models.ForeignKey(Beca)
    monto = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre
