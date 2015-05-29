from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'mpintegrations.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('home.urls')),
    url('', include('checkout.urls')),
    url('', include('notifications.urls')),
    url('', include('preferences.urls')),
    url('', include('profiles.urls')),
]
