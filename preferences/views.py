from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from libs.mercadopago import *
import os
import json
from .models import Preferences,PreferenceOptions

class PreferenceCreate(CreateView):
	model = Preferences
	template_name = 'preference_form.html'
	fields = ['title','quantity','unit_price','currency_id','picture_url','description','category_id','name','surname','email',
	'identification_type','identification_number','success','failure','pending','auto_return','excluded_payment_methods',
	'excluded_payment_types','installments','default_payment_method_id','default_installments',	'expires','expiration_date_from',
	'expiration_date_to','notification_url','external_reference','marketplace','marketplace_fee','additional_info',
	'differential_pricing',
	]

	
	def post(self, request, *args, **kwarg):
		self.object = None
		form = self.get_form()
		if form.is_valid():
			preference_model = form.save(commit=False)
			
			preference_model = self.get_preference(preference_model)

			preference_model.save()

			return redirect('preference_list')
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
				"identification":{
					"type":getattr(args,'identification_type'),
					"number":getattr(args,'identification_number'),
				}
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
			"marketplace" : getattr(args,'marketplace'),
			"marketplace_fee" : getattr(args,'marketplace_fee'),
			"additional_info" : getattr(args,'additional_info'),
			"differential_pricing" : getattr(args,'differential_pricing'),

		}

		mp = MP(os.environ['MP_CLIENT_ID'], os.environ['MP_CLIENT_SECRET'])

		preferenceResult = mp.create_preference(preference_data)

		sandbox_init_point = preferenceResult["response"]["sandbox_init_point"]
		init_point = preferenceResult["response"]["init_point"]
		setattr(args,'init_point',init_point)
		setattr(args,'sandbox_init_point',sandbox_init_point)
		
		return args


class PreferenceOptionsView(TemplateView):
	model = PreferenceOptions
	template_name = 'preferences_options.html'

	def post(self, request, *args, **kwarg):
		post_data = request.POST

		return HttpResponse(post_data)


	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super(PreferenceOptionsView, self).get_context_data(**kwargs)
	    # Get the fields names.
	    fields = Preferences.objects.all()
	    field_names = fields.model._meta.get_all_field_names()

	    context['field_names'] = field_names
	    return context

	def get_model_field(self):
		field_names = self.model._meta.get_all_field_names()

		return field_names




class PreferenceListView(ListView):
	model = Preferences
	queryset = Preferences.objects.order_by('-created_date')
	template_name = 'preference_list.html'
	context_object_name = 'prefence_list'
