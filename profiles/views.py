from django.views.generic import TemplateView, View, CreateView, DetailView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.models import User
from .forms import UserCreationEmailForm
from .models import Profile



from libs.mercadopago import *
import os
import json


# Create your views here.


class RegistrationFormView(CreateView):
	
	template_name = 'registration.html'
	form_class = UserCreationEmailForm
	success_url = reverse_lazy('home')

class UserProfileView(DetailView):

	template_name = 'profile.html'
	model = Profile


	
class MpRegistrationView(TemplateView):
	model = ''
	template_name = 'mp_registration.html'


class MpAuthorizationView(View):
	model = User
	template_name = 'mp_authorization.html'

	def get(self,request, **kwargs):
		data = self.get_authorization_data(data = self.request.GET)
		return render(request, self.template_name , {'data': data})

	def get_authorization_data(self,*args,**kwargs):
		data = kwargs.get('data')
		code = data['code']
		redirect_URI = 'http://127.0.0.1:8000/mp-authorization'
		mp = MP(os.environ['MP_CLIENT_ID'], os.environ['MP_CLIENT_SECRET'])
		params = { 'grant_type' : 'authorization_code', 'client_id' : os.environ['MP_CLIENT_ID'], 'client_secret' : os.environ['MP_CLIENT_SECRET'], 'code' : code, 'redirect_uri' : redirect_URI}


		response = mp.post('/oauth/token',None, params )
 		
		access_token = response['response']['access_token']
		refresh_token = response['response']['refresh_token']
		user_id = response['response']['user_id']
		public_key = response['response']['public_key']

		params = {'access_token':access_token}
		mp_user_data = mp.get('/users/me',params)

		email = mp_user_data['response']['email']

		return email

