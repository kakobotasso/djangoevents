#encoding: utf-8

from django.shortcuts import render#_to_response
from django.template import RequestContext
from django.http import HttpResponse
from forms import ContactForm

def home(request):
	context = {
		"nome": u"Kako",
		"email": u"kakodev@gmail.com"
	}
	#return render_to_response('home.html', context, RequestContext(request))#return HttpResponse(u'Hello World!!!')
	return render(request, "home.html", context)
	#o render retorna o request, o nome do template e o contexto

def contact(request):
	context = { }

	if request.method == 'POST':
		form = ContactForm( request.POST )
		if form.is_valid():
			context['data'] = form.cleaned_data

	else:
		form = ContactForm()
	context['form'] = form

	return render(request, "contact.html", context)

