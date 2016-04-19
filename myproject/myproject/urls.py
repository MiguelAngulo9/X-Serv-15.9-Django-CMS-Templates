from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^accounts/profile/$', 'cmstemplates.views.usuario'),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    #url(r'^cmstemplates/', 'cmstemplates.views.paginanueva'),
    url(r'^(\d+)', 'cmstemplates.views.index'),
    url(r'^annotated/$', 'cmstemplates.views.muestra_paginas'),
    url(r'^annotated/crear/$', 'cmstemplates.views.nuevo_recurso'),
    url(r'^admin/', include(admin.site.urls)),
)
