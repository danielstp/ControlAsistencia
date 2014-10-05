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


def Reporte(request):
  if request.GET.get('Colegios'):
            estudiantes= Estudiante.objects.filter(Colegio=request.GET.get('Colegios'))
"""
def FamiliarResponsable(request):
   
    return render(request, 'FamiliarResponsable.html',
                    {'estudiantes': estudiantes,
                    })

def Pagadores(request):
   
    return render(request, 'Pagadores.html',
                    {'estudiantes': estudiantes,
                    })

def AnadirPagador(request):
   
    return render(request, 'AnadirPagador.html',
                    {'estudiantes': estudiantes,
                    })

def ServiciosContratados(request):
   
   return render(request, 'ServiciosContratados.html',
                  {'estudiantes': estudiantes,
                   'Colegios': Colegio.objects.all(),
                   'Colegio':request.GET.get('Colegios'),
                  })

def BecaAlumno(request):
   
  return render(request, 'BecaAlumno.html',
                 {'estudiantes': estudiantes,
                 })

def ModifAsistenciasProg(request):
   
  return render(request, 'ModifAsistenciasProg.html',
                 {'estudiantes': estudiantes,
                  'Colegios': Colegio.objects.all(),
                  'Colegio':request.GET.get('Colegios'),
                 })

def ControlDeAsistencia(request):
  hoy=datetime.today()
  return render(request, 'ControlDeAsistencia.html',
                 {'estudiantes': estudiantes,
                  'Colegios': Colegio.objects.all(),
                  'Colegio':request.GET.get('Colegios'),
                  'hoy':hoy,
                  'menu': menu,
                 })

def InformeAsistencia(request):
   
  return render(request, 'InformeAsistencia.html',
                 {'estudiantes': estudiantes,
                  'Colegios': Colegio.objects.all(),
                  'Colegio':request.GET.get('Colegios'),
                  'curso': curso,
                 })

def Becas(request):
   
  return render(request, 'Becas.html',
                 {'becas': becas,
                  'menu': menu,
                 })
"""
def Reporte(request):

  if request.GET.get('colegio'):
            #estudiantes= Estudiante.objects.filter(Colegio=request.GET.get('colegio'))
            col =request.GET['colegio']
            #curs =request.GET['curso']
            diet =request.GET['dieta']
            #apell =request.GET['apellido']

            estudiantes= Estudiante.objects.filter(colegio=Colegio.objects.get(pk=col))#.filter(curso=Curso.objects.get(pk=curs))


  else:
            estudiantes= Estudiante.objects.all()




  return render(request, 'TareasEst.html', {'estudiantes': estudiantes,
                                            'Colegios': Colegio.objects.all(),
                                            'Cursos': Curso.objects.all(),
                                            'colegio':Colegio})
