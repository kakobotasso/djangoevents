# encoding: utf-8

from django.contrib import admin
from models import Event, Comment

class EventAdmin(admin.ModelAdmin):
	list_display = ['name', 'type', 'created_at']
	#lista de strings onde cada uma eh o nome do campo

	search_fields = ['name', 'type', 'description']


admin.site.register(Event, EventAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'event']
	search_fields = ['event__name', 'email']

admin.site.register(Comment, CommentAdmin)

