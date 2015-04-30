from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import HomeView


urlpatterns = [
    # Examples:
    # url(r'^$', 'mpintegrations.views.home', name='home'),
    url(r'^$', HomeView.as_view(), name='home'),

]
