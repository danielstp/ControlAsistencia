from django.conf.urls import patterns, include, url
from django.contrib import admin

from ControlAsistencia import views

urlpatterns = patterns('',

  url(r'^diario/$', views.diario, name='diario'),
  url(r'^mes$', views.mes, name='mes'),
  url(r'^asistencia$', views.listaAsist, name='Asistencia'),
  url(r'^registro$', views.RgAsist, name='Registro'),
  url(r'^reporte/$', views.Reporte, name='Reporte'),
  url(r'^$', views.index, name='index'),
#  url(r'^$', views.index, name='index'),
#   url(r'^$', views.index, name='index'),
#  url(r'^$', views.index, name='index'),
#  url(r'^$', views.index, name='index'),
#  url(r'^$', views.index, name='index'),
)
