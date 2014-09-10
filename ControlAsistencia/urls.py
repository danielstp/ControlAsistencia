from django.conf.urls import patterns, url

from ControlAsistencia import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ControlAsis.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', views.index, name='index'),
)
