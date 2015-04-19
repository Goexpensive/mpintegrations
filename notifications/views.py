from django.http import HttpResponse
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
	    data = self.get_resource_data(self.request)
	    json_data = self.post(data=data)

	    return HttpResponse(json_data,content_type='application/json')
	    
	
	def post(self, **kwargs):

			mp_id = kwargs.get('id')
			topic = kwargs.get('topic')

			notification = Notifications(mp_id = mp_id, topic = topic)
			notification.save()	

			return notification

