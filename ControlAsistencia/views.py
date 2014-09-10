from django.shortcuts import render
from django.http import HttpResponse
from ControlAsistencia import models


def index(request):
    estudiantes = models.Estudiante.objects.all()
    return render(request, 'ControlAsistencia/Estudiante.html', {'estudiantes': estudiantes})
