# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django import forms
from datetime import datetime
from ControlAsistencia.models import Estudiante, Centro, PlanAsistencia, Asistencia, Menu

import ControlAsistencia.views


 #widget=forms.Select(choices=Centro.objects.all())

def index(request):
  return render(request, 'Opciones.html')

def diario(request):
  lista=[]
  if request.GET.get('centros'):
    #return HttpResponse(request.GET.get('centros'))

    estudiantes= Estudiante.objects.filter(centro=request.GET.get('centros'))
  else:
    estudiantes= Estudiante.objects.all()

  return render(request, 'RepDiario.html',
                    {'estudiantes': estudiantes,
                     'centros': Centro.objects.all(),
                     'centro':request.GET.get('centros'),
                     'lista':lista})




def mes(request):
  return render(request, 'asistenciaDia.html', {'estudiantes': Estudiante.objects.all()})


def listaAsist (request):
  dicDays = {'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves',
    'FRIDAY':'viernes','SATURNDAY':'sabado','SUNDAY':'domingo'}
  hoy=datetime.today()
  diaSem=dicDays[hoy.strftime('%A').upper()]
  lista=[]
  if request.GET.get('centros'):
    #return HttpResponse(request.GET.get('centros'))

    estudiantes= Estudiante.objects.filter(centro=request.GET.get('centros'))

  else:
    estudiantes= Estudiante.objects.all()

  return render(request, 'asistenciaDia.html',
                    {'estudiantes': estudiantes,
                     'centros': Centro.objects.all(),
                     'centro':request.GET.get('centros'),
                     'lista':lista,
                     'hoy':hoy,
                     'diaSem':diaSem})

def RgAsist (request):
    asistieron=request.GET.getlist('asistio')
    menu = Menu.objects.get(pk=1)
    for asis in asistieron:
        asisten = Estudiante.objects.get(pk=asis)
        asi=Asistencia(asistente=asisten, fechaHora=datetime.today(), menu= menu)
        asi.save()
    return HttpResponse(asistieron)
    #
    #return render(request, 'registroDia.html', {'estudiantes': Estudiante.objects.all()})
def RepAsist(request):
    dicDays = {'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves',
        'FRIDAY':'viernes','SATURNDAY':'sabado','SUNDAY':'domingo'}
    hoy=datetime.today()
    diaSem=dicDays[hoy.strftime('%A').upper()]
    lista=[]
    if request.GET.get('centros'):
    #return HttpResponse(request.GET.get('centros'))

         estudiantes= Estudiante.objects.filter(centro=request.GET.get('centros'))
         asistencias= Asistencia.objects.filter()
         #for est in estudiantes



    else:
         estudiantes= Estudiante.objects.all()


    return render(request, 'asistenciaDia.html',
                    {'estudiantes': estudiantes,
                     'centros': Centro.objects.all(),
                     'centro':request.GET.get('centros'),
                     'lista':lista,
                     'hoy':hoy,
                     'diaSem':diaSem})