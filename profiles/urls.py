from django.conf.urls import url
from . import views

urlpatterns = [
    # ...
	url(r'sign-up$', views.ProfileCreateView.as_view(), name ='sign_up'),
	#url(r'^profile/(?P<pk>[\d]+)$', views.ProfileDetailView.as_view(), name = 'profile'),
	#url(r'^profile/(?P<pk>[\d]+)$', views.ProfileUpdateView.as_view(), name = 'profile_edit'),
	url(r'^profile/(?P<pk>[\d]+)$', views.ProfileView.as_view(), name = 'profile'),
]