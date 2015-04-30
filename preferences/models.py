from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Preferences(models.Model):
	title = models.CharField(max_length=255)
	quantity = models.IntegerField()
	unit_price = models.FloatField()
	currency_id = models.CharField(max_length=3)
	picture_url = models.URLField(null= True, blank=True)
	description = models.CharField(max_length=254, null= True, blank=True)
	category_id = models.CharField(max_length=254, null= True, blank=True)
	name =  models.CharField(max_length=254, null= True, blank=True)
	surname = models.CharField(max_length=254, null= True, blank=True)
	email = models.EmailField(max_length=254, null= True, blank=True)
	identification_type = models.CharField(max_length=254, null= True, blank=True)
	identification_number = models.CharField(max_length=254, null= True, blank=True)
	success =  models.URLField(null= True, blank=True)
	failure =  models.URLField(null= True, blank=True)
	pending =  models.URLField(null= True, blank=True)
	auto_return =  models.CharField(max_length=254, null= True, blank=True)
	excluded_payment_methods = models.CharField(max_length=254, null= True, blank=True)
	excluded_payment_types = models.CharField(max_length=254, null= True, blank=True)
	installments = models.IntegerField(null= True, blank=True)
	default_payment_method_id = models.CharField(max_length=254, null= True, blank=True)
	default_installments = models.IntegerField(null= True, blank=True)
	notification_url = models.URLField(max_length=255, blank=True)
	expires = models.NullBooleanField(blank=True)
	expiration_date_from = models.DateField(null= True, blank=True)
	expiration_date_to = models.DateField(null= True, blank=True)
	external_reference = models.CharField(max_length=255, blank=True)
	init_point = models.CharField(max_length=255, blank=True)
	sandbox_init_point = models.CharField(max_length=255, blank=True)
	created_date = models.DateTimeField(auto_now_add = True, blank = True)
	last_modified_date = models.DateTimeField(auto_now = True, blank = True)
	marketplace = models.CharField(max_length=255, null=True,blank=True)
	marketplace_fee = models.FloatField(blank=True, null=True)
	differential_pricing = models.IntegerField(blank=True,null=True)
	additional_info = models.CharField(max_length=600, null=True,blank=True)
	dimensions = models.CharField(max_length=255, null=True,blank=True)
	mode = models.CharField(max_length=255, null=True,blank=True) 
	local_pickup = models.NullBooleanField(blank=True)
	free_methods = models.IntegerField(null= True, blank=True)
	json = models.TextField(null=True,blank=True) 

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse('preference-detail', kwargs={'pk': self.pk})


class PreferenceTemplates(models.Model):
	name = models.CharField(max_length=255)
	list_fields = models.TextField()
	created_date = models.DateTimeField(auto_now_add = True, blank = True)

	def __str__(self):
		return str(self.name)
