# encoding: utf-8

from django.db import models

class Event(models.Model):
	TYPE_CHOICES = {
		(1, u'Workshop'),
		(2, u'Dojo'),
		(3, u'Palestra'),
	}

	#campos que este model vai ter
	name = models.CharField(verbose_name=u'Nome', max_length=100) #db_column = u'name_eventos'  #muda o nome da coluna no banco de dados
	type = models.IntegerField(choices=TYPE_CHOICES, verbose_name=u'Tipo do Evento') # primary_key=True #indica que é chave primária
	description = models.TextField(verbose_name=u'Descrição', blank=True)
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True)
	link = models.URLField(verbose_name=u'Link', blank=True)
	public = models.BooleanField(verbose_name=u'Público?', default=True)

	def comments_count(self):
		return self.comments.count();
	comments_count.short_description = u'Número de comentários'

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Evento'# Nome exibido no Django Admin
		verbose_name_plural = u'Eventos'
		ordering = ['name'] #ordem alfabetica pelo name
		#db_table = u'events' #altera o nome da tabela


class Comment(models.Model):
	name = models.CharField(verbose_name=u'Nome', max_length=100)
	email = models.EmailField(verbose_name=u'Email')
	event = models.ForeignKey(Event, verbose_name=u"Evento", related_name='comments')
	website = models.URLField(verbose_name="Site", blank=True)
	text = models.TextField(verbose_name=u'Texto')
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True)

	def __unicode__(self):
		return self.text

	class Meta:
		verbose_name = u'Comentário'
		verbose_name_plural = u'Comentários'
		ordering = ['created_at']