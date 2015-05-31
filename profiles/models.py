from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save



class Profile(models.Model):

	user = models.OneToOneField(User)
	mercadopago_user_id = models.BigIntegerField(blank=True, null=True)
	access_token = models.CharField(max_length=254, blank=True, null=True)
	public_key = models.CharField(max_length=254, blank=True, null=True)
	refresh_token = models.CharField(max_length=254, blank=True, null=True)
	mp_email = models.EmailField(max_length=254, blank=True, null=True)

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=User)





