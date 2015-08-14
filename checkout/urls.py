from django.conf.urls import url
from . import views

urlpatterns = [
    # ...

	url(r'checkout/$', views.CheckoutView.as_view(), name='checkout'),

]


    