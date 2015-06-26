from django.conf.urls import url
from . import views

urlpatterns = [
    # ...
	url(r'marketplace$', views.MarketplaceView.as_view(), name ='marketplace'),

]