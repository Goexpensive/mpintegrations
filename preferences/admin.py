from django.contrib import admin
from .models import *


@admin.register(Preferences)

class PreferencesAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity','unit_price','notification_url','external_reference','init_point','sandbox_init_point','created_date','last_modified_date')
