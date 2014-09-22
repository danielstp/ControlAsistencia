# -*- coding: utf-8 -*-
from django.shortcuts import render
from ControlAsistencia.models import Estudiante

import ControlAsistencia.views
import django_tables2 as tables


def index(request):
  return render(request, 'Opciones.html')

def diario(request):
  return render(request, 'Estudiante.html', {'estudiantes': Estudiante.objects.all()})

def mes(request):
  return render(request, 'Estudiante.html', {'estudiantes': Estudiante.objects.all()})
