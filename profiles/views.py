from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from braces.views import LoginRequiredMixin

from django.contrib.auth.models import User
from .forms import UserCreationEmailForm
from .models import Profile

from django.contrib.auth.forms import UserCreationForm



from libs.mercadopago import *
import os
import json



class ProfileCreateView(CreateView):

	template_name = 'registration.html'
	form_class = UserCreationForm

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		self.object = User.objects.create(username=username)
		self.object.set_password(password)
		self.object.save()
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return HttpResponseRedirect(self.get_success_url())
	
	def get_success_url(self): 
		return reverse('profile',args=(self.object.profile.id,))


class  ProfileView(LoginRequiredMixin, View):
	model = Profile
	template_name = 'profile.html'

	login_url = "/sign-up/"
	redirect_field_name = "hollaback"
	raise_exception = True

	def get(self,request, *args, **kwargs):
		
		user_profile = self.get_authorization(data = self.request.GET, pk = kwargs['pk'])
		
		return render(request, self.template_name , {'profile': user_profile})

	def mp_update_profile(self, *args, **kwargs):

		user_profile = kwargs['user_profile']
		mp_data = self.get_authorization_data(code = kwargs['code'], pk = user_profile.id)
		user_profile.mp_email = mp_data['mp_email']
		user_profile.mercadopago_user_id = mp_data['mercadopago_user_id']
		user_profile.access_token = mp_data['access_token']
		user_profile.public_key = mp_data['public_key']
		user_profile.refresh_token = mp_data['refresh_token']
		print(user_profile.refresh_token)
		user_profile.save()

		return user_profile

	def get_authorization(self,*args,**kwargs):

		user_profile = Profile.objects.get(pk = kwargs['pk'])
		data = kwargs.get('data')
		
		if 'code' in data:
			code = data['code']
			user_profile = self.mp_update_profile(code = code, user_profile = user_profile)
			
		return user_profile

	def get_authorization_data(self,*args,**kwargs):

		code = kwargs.get('code')
		pk = kwargs.get('pk')
		redirect_URI = 'http://127.0.0.1:8000/profile/{}'.format(pk)
		mp = MP(os.environ['MP_CLIENT_ID'], os.environ['MP_CLIENT_SECRET'])
		params = { 'grant_type' : 'authorization_code', 'client_id' : os.environ['MP_CLIENT_ID'], 'client_secret' : os.environ['MP_CLIENT_SECRET'], 'code' : code, 'redirect_uri' : redirect_URI}
		response = mp.post('/oauth/token',None, params )
		access_token = response['response']['access_token']
		refresh_token = response['response']['refresh_token']
		mercadopago_user_id = response['response']['user_id']
		public_key = response['response']['public_key']
		params = {'access_token':access_token}
		mp_user_data = mp.get('/users/me',params)
		mp_email = mp_user_data['response']['email']

		mp_data = {'access_token':access_token, 'refresh_token': refresh_token,'mercadopago_user_id' : mercadopago_user_id, 'public_key' : public_key, 'mp_email': mp_email}

		return mp_data

