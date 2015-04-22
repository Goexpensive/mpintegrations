from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from .models import Notifications


class NotificationListView(ListView):

	model = Notifications
	template_name = 'notifications_list.html'
	context_object_name = 'notifications_list'

class NotificationView(View):
	model = Notifications
	template_name = 'notificatons_test.html'
	fields=['id','topic']
	id = int()
	topic = str()

	def get(self,request, **kwargs):
			notification = 'No hay nuevas notificaciones'
			return render(request, 'notification_test.html', {'data':notification})
	
	def post(self,request, **kwargs):
		data = self.get_data(data = self.request.GET)
		if self.is_valid(data):
			notification = Notifications(id = self.id, topic = self.topic)
			notification.save()
			return render(request, 'notification_test.html', {'data':notification})
		else:
			notification = 'No hay nuevas notificaciones'
			return render(request, 'notification_test.html', {'data':notification})

	def get_data(self,*args,**kwargs):
		listnotif = kwargs.get('data')
		data = dict()
		for field in self.fields:
			data[field] = listnotif.get(field)

		return data

	def is_valid(self,args):
		i = 0
		id = args['id']
		topic = args['topic']
		if ((id is not None) and (topic is not None)):
			self.id = int(id)
			self.topic = str(topic)
			return True
		else: 
			return False	 




