# -*- coding: utf-8 -*-
from django.contrib import admin

from admin_exporter.actions import export_as_csv_action
from admin_exporter.actions import export_as_json_action
from admin_exporter.actions import export_as_xml_action
from admin_exporter.actions import export_as_yaml_action


from ControlAsistencia.models import Estudiante
from ControlAsistencia.models import Tutor
from ControlAsistencia.models import Pago
from ControlAsistencia.models import Asistencia
from ControlAsistencia.models import Menu
from ControlAsistencia.models import TipoMenu
from ControlAsistencia.models import Colegio
from ControlAsistencia.models import Direccion
from ControlAsistencia.models import Beca
from ControlAsistencia.models import Becado
from ControlAsistencia.models import BecaColegio
from ControlAsistencia.models import Provincia
from ControlAsistencia.models import Contacto
from ControlAsistencia.models import Persona
from ControlAsistencia.models import Telefono
from ControlAsistencia.models import Pagador
from ControlAsistencia.models import Banco
from ControlAsistencia.models import CuentaBanco
from ControlAsistencia.models import Etapa
from ControlAsistencia.models import ComunidadAutonoma
from ControlAsistencia.models import PlanAsistencia
from ControlAsistencia.models import Documento
from ControlAsistencia.models import Curso


class EstudianteEnLinea(admin.TabularInline):
    model = Estudiante
    fk_name = 'tutor'
    extra = 1


class PlanAsistenciaEnLinea(admin.TabularInline):
    model = PlanAsistencia


class DocumentoEnLinea(admin.TabularInline):
    model = Documento
    extra = 1


class TutorAdmin(admin.ModelAdmin):
    inlines = [EstudianteEnLinea]


class DireccionEnLinea(admin.TabularInline):
    model = Direccion


class EstudianteAdmin(admin.ModelAdmin):
    inlines = [DocumentoEnLinea,PlanAsistenciaEnLinea]


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Pago)
admin.site.register(Asistencia)
admin.site.register(TipoMenu)
admin.site.register(Menu)
admin.site.register(Colegio)
admin.site.register(Direccion)
admin.site.register(Beca)
admin.site.register(Becado)
admin.site.register(BecaColegio)
admin.site.register(Provincia)
admin.site.register(Persona)
admin.site.register(Contacto)
admin.site.register(Telefono)
admin.site.register(Pagador)
admin.site.register(Banco)
admin.site.register(CuentaBanco)
admin.site.register(Documento)
admin.site.register(Etapa)
admin.site.register(ComunidadAutonoma)
admin.site.register(PlanAsistencia)
admin.site.register(Curso)

admin.site.add_action(export_as_csv_action)
admin.site.add_action(export_as_json_action)
admin.site.add_action(export_as_xml_action)
admin.site.add_action(export_as_yaml_action)
