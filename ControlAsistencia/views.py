# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django import forms
from datetime import datetime, date
from ControlAsistencia.models import Estudiante, Colegio, PlanAsistencia, Asistencia, Menu, Curso


def index(request):
  return render(request, 'Opciones.html')

def diario(request):
  lista=[]
  if request.GET.get('Colegios'):
    #return HttpResponse(request.GET.get('Colegios'))
    estudiantes= Estudiante.objects.filter(Colegio=request.GET.get('Colegios'))
  else:
    estudiantes= Estudiante.objects.all()

  return render(request, 'RepDiario.html',
                    {'estudiantes': estudiantes,
                     'Colegios': Colegio.objects.all(),
                     'Colegio':request.GET.get('Colegios'),
                     'lista':lista})




def mes(request):
  return render(request, 'asistenciaDia.html', {'estudiantes': Estudiante.objects.all()})


def listaAsist (request):
  dicDays = {'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves',
    'FRIDAY':'viernes','SATURNDAY':'sabado','SUNDAY':'domingo'}
  hoy=datetime.today()
  diaSem=dicDays[hoy.strftime('%A').upper()]
  lista=[]
  if request.GET.get('Colegios'):
    #return HttpResponse(request.GET.get('Colegios'))

    estudiantes= Estudiante.objects.filter(Colegio=request.GET.get('Colegios'))

  else:
    estudiantes= Estudiante.objects.all()

  return render(request, 'asistenciaDia.html',
                    {'estudiantes': estudiantes,
                     'Colegios': Colegio.objects.all(),
                     'Colegio':request.GET.get('Colegios'),
                     'lista':lista,
                     'hoy':hoy,
                     'diaSem':diaSem})

def RgAsist (request):
    dicDays = {'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves',
    'FRIDAY':'viernes','SATURNDAY':'sabado','SUNDAY':'domingo'}
    hoy=datetime.today()
    diaSem=dicDays[hoy.strftime('%A').upper()]
    asistieron=request.GET.getlist('asistio')
    if request.GET.get('Colegios'):
            estudiantes= Estudiante.objects.filter(Colegio=request.GET.get('Colegios'))

    else:
            estudiantes= Estudiante.objects.all()
    menu = Menu.objects.get(pk=1)
    for asis in asistieron:
        asisten = Estudiante.objects.get(pk=asis)
        asi=Asistencia(asistente=asisten, fecha=date.today(), menu= menu)
        asi.save()
    asistencias= Asistencia.objects.filter(fecha=date.today())
    return render(request, 'registroDia.html',
                    {'estudiantes': estudiantes,
                     'Colegios': Colegio.objects.all(),
                     'Colegio':request.GET.get('Colegios'),
                     'hoy':hoy,
                     'diaSem':diaSem,
                     'asistencias':asistencias })


    #
    #return render(request, 'registroDia.html', {'estudiantes': Estudiante.objects.all()})
def RepAsist(request):
    dicDays = {'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves',
        'FRIDAY':'viernes','SATURNDAY':'sabado','SUNDAY':'domingo'}
    hoy=datetime.today()
    diaSem=dicDays[hoy.strftime('%A').upper()]
    lista=[]
    if request.GET.get('Colegios'):
    #return HttpResponse(request.GET.get('Colegios'))

         estudiantes= Estudiante.objects.filter(Colegio=request.GET.get('Colegios'))
         asistencias= Asistencia.objects.filter(fecha=date.today())
         #for est in estudiantes



    else:
         estudiantes= Estudiante.objects.all()


    return render(request, 'RepDiario.html',
                    {'estudiantes': estudiantes,
                     'Colegios': Colegio.objects.all(),
                     'Colegio':request.GET.get('Colegios'),
                     'lista':lista,
                     'hoy':hoy,
                     'diaSem':diaSem})

def tarea(request):

  return render(request, 'TareasEst.html', {'estudiantes': Estudiante.objects.all(),
                                            'Colegios': Colegio.objects.all(),
                                            'Cursos': Curso.objects.all()})