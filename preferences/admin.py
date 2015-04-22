from django.contrib import admin
from .models import *


@admin.register(Preferences)

class PreferencesAdmin(admin.ModelAdmin):
	list_display = (
		'title','quantity','unit_price','currency_id','picture_url','description','category_id','name','surname','email','success','failure',
		'pending','auto_return','excluded_payment_methods','excluded_payment_types','installments','default_payment_method_id',
		'default_installments','expires','expiration_date_from','expiration_date_to','notification_url','external_reference',
		'init_point','sandbox_init_point','created_date','last_modified_date')
