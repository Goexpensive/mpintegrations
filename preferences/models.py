from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Preferences(models.Model):
	items_title = models.CharField(max_length=255)
	items_quantity = models.CharField(max_length=255)
	items_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
	notification_url = models.CharField(max_length=255)
	external_reference = models.CharField(max_length=255)
	init_point = models.CharField(max_length=255)
	sandbox_init_point = models.CharField(max_length=255)
	created_date = models.DateTimeField(auto_now_add = True, blank = True)
	last_modified_date = models.DateTimeField(auto_now = True, blank = True)

	def __str__(self):
		return str(self.items_title)

	def get_absolute_url(self):
		return reverse('preference-detail', kwargs={'pk': self.pk})