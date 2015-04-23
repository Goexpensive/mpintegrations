from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'mpintegrations.views.home', name='home'),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),

]
