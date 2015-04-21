from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Notifications(models.Model):
	id = models.BigIntegerField(primary_key=True)
	topic = models.CharField(max_length=255)
	created_date = models.DateTimeField(auto_now_add = True, null = True)
	last_modified_date = models.DateTimeField(auto_now = True, null = True)

	def __str__(self):
		return str(self.id)
	

