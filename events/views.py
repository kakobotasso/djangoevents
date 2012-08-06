# encoding: utf-8

from django.shortcuts import render, get_object_or_404
from models import Event

def index(request):
	template_name = 'events/index.html'
	context = {}
	context['events'] = Event.objects.all()
	return render(request, template_name, context)

def details(request, pk):
	event = get_object_or_404(Event, pk=pk)
	template_name = 'events/details.html'
	context = {
		'event' : event
	}
	return render(request, template_name, context)