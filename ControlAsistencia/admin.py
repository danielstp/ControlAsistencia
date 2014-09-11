from django.contrib import admin
from ControlAsistencia.models import Estudiante
from ControlAsistencia.models import Tutor
from ControlAsistencia.models import Pago
from ControlAsistencia.models import Asistio
from ControlAsistencia.models import Menu
from ControlAsistencia.models import Centro
from ControlAsistencia.models import Direccion
from ControlAsistencia.models import Beca
from ControlAsistencia.models import Nombre
from ControlAsistencia.models import Becario
from ControlAsistencia.models import BecaCentro
from ControlAsistencia.models import Provincia


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
admin.site.register(Asistio)
admin.site.register(Menu)
admin.site.register(Centro)
admin.site.register(Direccion)
admin.site.register(Beca)
admin.site.register(Becario)
admin.site.register(BecaCentro)
admin.site.register(Nombre)
admin.site.register(Provincia)



