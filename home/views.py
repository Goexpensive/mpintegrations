from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from preferences.models import PreferenceTemplates

from libs.mercadopago import *
import os
import json


class HomeView(TemplateView):
	model = PreferenceTemplates
	template_name = 'home.html'
	
	def get_context_data(self, **kwargs):
		
		context = super(HomeView, self).get_context_data(**kwargs)
		context['preference_templates'] = self.model.objects.all().order_by('-created_date')[:3]

		return context
