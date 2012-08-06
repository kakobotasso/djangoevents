# encoding: utf-8

from django.contrib import admin
from django.http import HttpResponse
from models import Event, Comment

def mark_private(modeladmin, request, queryset):
	queryset.update(public=False)
	modeladmin.message_user(request, u'Eventos atualizados com sucesso')
	#return HttpResponse(u"OK") #Pode ser utilizado para retornar o que quisermos

mark_private.short_description = u'Marcar eventos como privados'

def mark_public(modeladmin, request, queryset):
	queryset.update(public=True)
	modeladmin.message_user(request, u'Eventos atualizados com sucesso')

mark_public.short_description = u'Marcar eventos como públicos'

class EventAdmin(admin.ModelAdmin):
	list_display = ['name', 'type','comments_count', 'public', 'created_at']
	#lista de strings onde cada uma eh o nome do campo

	search_fields = ['name', 'type', 'description']

	actions = [mark_private, mark_public]


admin.site.register(Event, EventAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'event']
	search_fields = ['event__name', 'email']

admin.site.register(Comment, CommentAdmin)

