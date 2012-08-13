# encoding: utf-8

from django import forms

class ContactForm(forms.Form):
	name = forms.CharField( label=u'Nome', required=True )
	email = forms.EmailField( label=u'E-mail', required=True )
	message = forms.CharField( label=u'Mensagem', widget=forms.Textarea )