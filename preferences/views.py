from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.forms.models import model_to_dict
from libs.mercadopago import *
import os
import json
from .models import Preferences

class PreferenceCreate(CreateView):
	model = Preferences
	template_name = 'preference_form.html'
	fields = ['items_title','items_quantity','items_unit_price','notification_url','external_reference']
	preference_fields = ["items","payer","back_urls","auto_return","payment_methods","shipments","notification_url","external_reference",
					"expires","expiration_date_from","expiration_date_to",
	]

	def post(self, request, *args, **kwarg):
		form = self.get_form()
		if form.is_valid():
			preference_model = form.save(commit=False)
			
			preference = self.get_preference(form_list=preference_model)
			preference = json.dumps(preference, ensure_ascii=False)
			return HttpResponse(preference)
		else:
			return self.form_invalid(form)

	def get_preference(self,*args,**kwarg):
		preference = dict()
		form_list = kwarg.get('form_list')
		form_list = model_to_dict(form_list)
		keys = form_list.keys()
		for field in keys:
			for key in self.preference_fields:
				if (key in field and key != field):
					preference[key] =  dict()
					preference[key][field] = form_list[field]
		
		return preference



class PreferenceUpdate(UpdateView):
	model = Preferences
	fields = ['items_title']

class PreferenceDelete(DeleteView):
	model = Preferences
	success_url = reverse_lazy('preference-list')