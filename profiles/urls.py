from django.conf.urls import url
from .views import MpRegistrationView,MpAuthorizationView,RegistrationFormView,UserProfileView

urlpatterns = [
    # ...
	url(r'sign-up$', RegistrationFormView.as_view(), name ='sign_up'),
	url(r'mp-sign-up$', MpRegistrationView.as_view(), name ='mp_sign_up'),
	url(r'mp-authorization$', MpAuthorizationView.as_view(), name ='mp_authorization'),
	url(r'^profile/(?P<pk>[\d]+)$', UserProfileView.as_view(), name = 'profile'),
]