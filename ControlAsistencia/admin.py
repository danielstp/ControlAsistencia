from django.contrib import admin
from ControlAsistencia.models import Estudiante
from ControlAsistencia.models import Tutor
from ControlAsistencia.models import Pago
from ControlAsistencia.models import Asistio
from ControlAsistencia.models import Menu
from ControlAsistencia.models import Centro

class EstudianteEnLinea(admin.TabularInline):
    model = Estudiante
    
class TutorAdmin(admin.ModelAdmin):
    inlines = [EstudianteEnLinea]
    
admin.site.register(Estudiante)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Pago)
admin.site.register(Asistio)
admin.site.register(Menu)
admin.site.register(Centro)
