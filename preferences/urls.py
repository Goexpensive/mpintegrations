from django.conf.urls import url
from .views import PreferenceCreate,PreferenceOptionsView,PreferenceListView

urlpatterns = [
    # ...
    url(r'preference/$', PreferenceOptionsView.as_view(), name='preference'),
    url(r'preference/add/$', PreferenceCreate.as_view(), name='preference_add'),
    url(r'preference/list/$', PreferenceListView.as_view(), name='preference_list'),
]

