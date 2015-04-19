from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Notifications(models.Model):
	mp_id = models.PositiveIntegerField()
	topic = models.CharField(max_length=255)
	

