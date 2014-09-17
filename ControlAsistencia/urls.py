from django.conf.urls import patterns, url

from ControlAsistencia import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
)
