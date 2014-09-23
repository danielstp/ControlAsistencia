# -*- coding: utf-8 -*-
from django.shortcuts import render
from ControlAsistencia.models import Estudiante, Centro

import ControlAsistencia.views
import django_tables2 as tables


def index(request):
  return render(request, 'Opciones.html')

def diario(request):
  lista = []
  return render(request, 'RepDiario.html', {'estudiantes': Estudiante.objects.all(), 'centros': Centro.objects.all(), 'lista':lista})

def mes(request):
  return render(request, 'RepMensual.html', {'estudiantes': Estudiante.objects.all()})
