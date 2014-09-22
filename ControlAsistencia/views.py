# -*- coding: utf-8 -*-
from django.shortcuts import render
from ControlAsistencia.models import Estudiante

import ControlAsistencia.views
import django_tables2 as tables


def index(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'Estudiante.html', {'estudiantes': Estudiante.objects.all()})
