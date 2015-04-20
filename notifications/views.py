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

	def get(self, request, **kwargs):
		data = self.request.GET
		saved_data = self.post(data=data)

		return render(request, 'notification_test.html', {'data':saved_data})

	
	def post(self, **kwargs):

			get_notif = kwargs.get('data')
			mp_id = get_notif.get('id')
			topic = get_notif.get('topic')

			notification = Notifications(mp_id = mp_id, topic = topic)
			notification.save()	

			return notification

