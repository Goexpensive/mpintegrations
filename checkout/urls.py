from django.conf.urls import patterns, include, url
from django.contrib import admin
from checkout.views import CheckoutView


urlpatterns = patterns('',

    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),

)
    