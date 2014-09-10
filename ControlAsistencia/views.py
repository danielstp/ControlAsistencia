from django.shortcuts import render
from django.http import HttpResponse
import ControlAsistencia


def index(request):
    estudiantes = ControlAsistencia.models.Estudiante.objects.all()
    return render(request, 'ControlAsistencia/Estudiante.html', {'estudiantes': estudiantes})
