from django.conf.urls import url
from .views import PreferenceCreate,PreferencesCustomView,PreferenceListView

urlpatterns = [
    # ...
    url(r'preference/$', PreferencesCustomView.as_view(), name='preference'),
    url(r'preference/add/(?P<filters>\w+)$', PreferenceCreate.as_view(), name='preference_add'),
    url(r'preference/list/$', PreferenceListView.as_view(), name='preference_list'),
]

