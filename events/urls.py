# encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
	url(r'^$', 'index', name="events"),
	url(r'^(?P<pk>\d+)/$', 'details', name="events_details"), # \d siginifica que posso colocar mais de um caracter numerico na URL. Para escrever alfanumericos é \w
)