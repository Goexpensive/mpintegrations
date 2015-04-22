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
	fields = ['title','quantity','unit_price','currency_id','picture_url','description','category_id','name','surname','email','success','failure',
	'pending','auto_return','excluded_payment_methods','excluded_payment_types','installments','default_payment_method_id','default_installments',
	'expires','expiration_date_from','expiration_date_to','notification_url','external_reference',
	]

	
	def post(self, request, *args, **kwarg):
		form = self.get_form()
		if form.is_valid():
			preference_model = form.save(commit=False)
			
			preference_data = self.get_preference(preference_model)
			
			return HttpResponse(preference_data)
		else:
			return self.form_invalid(form)
	
	def get_preference(self,args):
		preference_data = []
		#getattr(args, = kwarg.get('getattr(args,'),
		preference_data = {
			"items" : [{
				"id" : getattr(args, 'id'),
				"title" : getattr(args, 'title'),
				"currency_id" : getattr(args,'currency_id'),
				"picture_url" : getattr(args,'picture_url'),
				"description" : getattr(args,'description'),
				"category_id" : getattr(args,'category_id'),
				"quantity" : 	getattr(args,'quantity'),
				"unit_price" : 	getattr(args,'unit_price'),
			}],
			"payer" : {
				"name" : getattr(args,'name'),
				"surname" : getattr(args,'surname'),
				"email" : getattr(args,'email'),
			},
			"back_urls" : {
				"success" : getattr(args,'success'),
				"failure" : getattr(args,'failure'),
				"pending" : getattr(args,'pending'),
			},
			"auto_return" : getattr(args,'auto_return'),
			"payment_methods" : {
				"excluded_payment_methods" :[
					{
						"id" : getattr(args,'excluded_payment_methods'),
					}
				],
				"excluded_payment_types" : [
					{
						"id" : getattr(args,'excluded_payment_types'),
					}
				],
				"installments" : getattr(args,'installments'),
				"default_payment_method_id" : getattr(args,'default_payment_method_id'),
				"default_installments" :getattr(args,'default_installments'),
			},
			"notification_url" : getattr(args,'notification_url'),
			"external_reference" : getattr(args,'external_reference'),
			"expires" : getattr(args,'expires'),
			"expiration_date_from" : getattr(args,'expiration_date_from'),
			"expiration_date_to" : getattr(args,'expiration_date_to'),
		}

		mp = MP(os.environ['MP_CLIENT_ID'], os.environ['MP_CLIENT_SECRET'])

		preferenceResult = mp.create_preference(preference_data)

		url = preferenceResult["response"]["sandbox_init_point"]

		
		
		return url


class PreferenceUpdate(UpdateView):
	model = Preferences
	fields = ['title']

class PreferenceDelete(DeleteView):
	model = Preferences
	success_url = reverse_lazy('preference-list')