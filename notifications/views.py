from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from .models import Notifications

from libs.mercadopago import *
import os
import json


class NotificationListView(ListView):

	model = Notifications
	queryset = Notifications.objects.order_by('-created_date')
	template_name = 'notifications_list.html'
	context_object_name = 'notifications_list'


class NotificationView(View):
	model = Notifications
	template_name = 'notificatons_test.html'
	fields=['id','topic']
	id = int()
	topic = str()

	def get(self,request, **kwargs):
		data = self.get_data(data = self.request.GET)
		if self.is_valid(data):
			notification_info = self.get_notification_data(self.id,self.topic)
			notification = Notifications(mp_id = self.id, topic = self.topic, notification_json = notification_info)
			notification.save()
			return render(request, 'notification_test.html', {'data':notification})
		else:
			notification = 'No hay nuevas notificaciones'
			return render(request, 'notification_test.html', {'data':notification})
	
	def post(self,request, **kwargs):
		data = self.get_data(data = self.request.GET)
		if self.is_valid(data):
			notification_info = self.get_notification_data(self.id,self.topic)
			notification = Notifications(mp_id = self.id, topic = self.topic, notification_json = notification_info)
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

	def get_notification_data(self,id,topic):
		mp = MP(os.environ['MP_CLIENT_ID'], os.environ['MP_CLIENT_SECRET'])
		notification_info = []
		if topic == 'payment':
			notification_info = mp.get("/collections/notifications/" + str(id) )
		
		if topic == 'merchant_order':
			notification_info = mp.get("/merchant_orders/" + str(id) )
		
		return notification_info	


		






