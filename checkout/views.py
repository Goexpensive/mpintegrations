from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView


from libs.mercadopago import *
import json
import os

# Create your views here.

class  CheckoutView(View):
	template_name = 'checkout.html'

	def get(self,request, *args, **kwargs):

			
		return render(request, self.template_name, {'public_key': os.environ['MP_PUBLIC_KEY']})
	
	def post(self,request, *args, **kwargs):


		payment_data = self.request.POST
		print(self.request.POST)
		mp = MP(os.environ['MP_SECRET_KEY'])
		payment = mp.post("/v1/payments", {
	        "transaction_amount": payment_data['transaction_amount'],
	        "token": payment_data['token'],
	        "description": "Title of what you are paying for",
	        "payer": {
	            "email": payment_data['email']
	        },
	        "installments": int(payment_data['installments']),
	        "payment_method_id": payment_data['paymentMethodId'],
	       	#"issuer_id": 338
	    });
		print(payment)
		#if payment['status']==201:
		#	payment = payment['response']
		

		return render(request,'payments.html', {'result':payment} )

