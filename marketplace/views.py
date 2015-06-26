from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView

from profiles.models import Profile
from django.contrib.auth.models import User

import os

# Create your views here.

class  MarketplaceView(View):
	model = User
	template_name = 'marketplace_cart.html'

	@csrf_exempt
	def get(self,request, *args, **kwargs):

		sellers = self.model.objects.all().order_by('-date_joined')[:3]
			
		return render(request, self.template_name, {'sellers': sellers, 'public_key': os.environ['MP_PUBLIC_KEY']})
