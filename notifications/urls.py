from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from .views import NotificationView,NotificationListView


urlpatterns = patterns('',

	url(r'^notification/test/$', csrf_exempt(NotificationView.as_view()), name='notification_test'),
	url(r'^notification/list/$', NotificationListView.as_view(), name='notification_list'),

)