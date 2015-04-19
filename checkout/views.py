from django.views.generic import TemplateView
from libs.mercadopago import *
import dateutil.parser
import json
import os

class CheckoutView(TemplateView):
	model = ''
	template_name = 'checkout.html'

	def get_context_data(self, **kwargs):
		preference = {
			"items": [
				{
					"title": "Multicolor kite",
					"quantity": 1,
					"currency_id": "ARS", # Available currencies at: https://api.mercadopago.com/currencies
					"unit_price": 10.0
				}
			]
		}

		mp = MP(os.environ['MP_CLIENT_ID'], os.environ['MP_CLIENT_SECRET'])

		preferenceResult = mp.create_preference(preference)

		url = preferenceResult["response"]["sandbox_init_point"]

		context = super(CheckoutView, self).get_context_data(**kwargs)

		context['url'] = url

		return context

