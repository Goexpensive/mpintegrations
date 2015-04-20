from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from libs.mercadopago import *
import os
import json
from .models import Preferences

class PreferenceCreate(CreateView):
	model = Preferences
	template_name = 'preference_form.html'
	fields = ['title','quantity','unit_price','notification_url','external_reference']

	def post(self, request, *args, **kwarg):
		form = self.get_form()
		if form.is_valid():
			preference_model = form.save(commit=False)
			preference = {
				"items": [
					{
						"title": str(preference_model.title),
						"quantity": int(preference_model.quantity),
						"currency_id": "ARS", # Available currencies at: https://api.mercadopago.com/currencies
						"unit_price": float(preference_model.unit_price)
					}
				]
				#"notification_url": preference_model.notification_url
			}

			mp = MP(os.environ['MP_CLIENT_ID'], os.environ['MP_CLIENT_SECRET'])
			preferenceResult = mp.create_preference(preference)
			
			sandbox_init_point = preferenceResult["response"]["sandbox_init_point"]
			init_point = preferenceResult["response"]["init_point"]
			
			preference_model.sandbox_init_point = sandbox_init_point
			preference_model.init_point = init_point
			preference_model.save() 

			#Crear metodo para la creacion de la preferencia.
			#Crear Succes template.

			return HttpResponse(preference_model,content_type='application/json')
		else:
			return self.form_invalid(form)
			



class PreferenceUpdate(UpdateView):
	model = Preferences
	fields = ['title']

class PreferenceDelete(DeleteView):
	model = Preferences
	success_url = reverse_lazy('preference-list')