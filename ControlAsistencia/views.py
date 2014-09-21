# -*- coding: utf-8 -*-
from django.shortcuts import render

import ControlAsistencia


def index(request):
    estudiantes = ControlAsistencia.models.Estudiante.objects.all()
    return render(request, 'Estudiante.html', {'estudiantes': estudiantes})
