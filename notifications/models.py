from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Notifications(models.Model):
	mp_id = models.BigIntegerField()
	topic = models.CharField(max_length=255)
	created_date = models.DateTimeField(auto_now_add = True, blank = True)
	last_modified_date = models.DateTimeField(auto_now = True, blank = True)

	def __str__(self):
		return str(self.mp_id)
	

