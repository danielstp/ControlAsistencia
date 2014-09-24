# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django import forms
from ControlAsistencia.models import Estudiante, Centro

import ControlAsistencia.views


 #widget=forms.Select(choices=Centro.objects.all())

def index(request):
  return render(request, 'Opciones.html')

def diario(request):
  if request.GET.get('centros'):
    estudiantes= Estudiante.objects.filter(centro=request.GET.get('centros'))
  else:
    estudiantes= Estudiante.objects.all()

  return render(request, 'RepDiario.html',
                    {'estudiantes': Estudiante.objects.all(),
                     'centros': Centro.objects.all(),
                     'centro':request.GET.get('centros')})

def diario1(request, centro):
  cen=centro
  return HttpResponse("You're looking at the results of poll %s." % cen)


def mes(request):
  return render(request, 'RepMensual.html', {'estudiantes': Estudiante.objects.all()})
