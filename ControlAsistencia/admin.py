# -*- coding: utf-8 -*-
from django.contrib import admin

from ControlAsistencia.models import Estudiante
from ControlAsistencia.models import Tutor
from ControlAsistencia.models import Pago
from ControlAsistencia.models import Asistencia
from ControlAsistencia.models import Menu
from ControlAsistencia.models import Centro
from ControlAsistencia.models import Direccion
from ControlAsistencia.models import Beca
from ControlAsistencia.models import Becado
from ControlAsistencia.models import BecaCentro
from ControlAsistencia.models import Provincia
from ControlAsistencia.models import Contacto
from ControlAsistencia.models import Persona
from ControlAsistencia.models import Telefono
from ControlAsistencia.models import Pagador
from ControlAsistencia.models import Banco
from ControlAsistencia.models import CuentaBanco

class EstudianteEnLinea(admin.TabularInline):
    model = Estudiante


class TutorAdmin(admin.ModelAdmin):
    inlines = [EstudianteEnLinea]


class DireccionEnLinea(admin.TabularInline):
    model = Direccion


class EstudianteAdmin(admin.ModelAdmin):
    inlines = [DireccionEnLinea]


admin.site.register(Estudiante)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Pago)
admin.site.register(Asistencia)
admin.site.register(Menu)
admin.site.register(Centro)
admin.site.register(Direccion)
admin.site.register(Beca)
admin.site.register(Becado)
admin.site.register(BecaCentro)
admin.site.register(Provincia)
admin.site.register(Persona)
admin.site.register(Contacto)
admin.site.register(Telefono)
admin.site.register(Pagador)
admin.site.register(Banco)
admin.site.register(CuentaBanco)