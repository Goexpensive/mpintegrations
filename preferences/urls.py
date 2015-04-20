from django.conf.urls import url
from .views import PreferenceCreate, PreferenceUpdate, PreferenceDelete

urlpatterns = [
    # ...
    url(r'preference/add/$', PreferenceCreate.as_view(), name='preference_add'),
    url(r'preference/(?P<pk>[0-9]+)/$', PreferenceUpdate.as_view(), name='preference_update'),
    url(r'preference/(?P<pk>[0-9]+)/delete/$', PreferenceDelete.as_view(), name='preference_delete'),
]

