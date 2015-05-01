from django.conf.urls import url
from .views import PreferenceCreate,PreferencesTemplateView,PreferenceListView

urlpatterns = [
    # ...
	url(r'preference/template$', PreferencesTemplateView.as_view(), name='preference_template'),
	url(r'preference/add/$', PreferenceCreate.as_view(), name='preference_add'),
	url(r'preference/add/(?P<filters>[\w-]+)$', PreferenceCreate.as_view(), name='preference_add_custom'),
	url(r'preference/list/$', PreferenceListView.as_view(), name='preference_list'),
]

