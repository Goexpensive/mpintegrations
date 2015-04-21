from django.contrib import admin
from .models import *


@admin.register(Notifications)

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic','created_date','last_modified_date')

