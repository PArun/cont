from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cont.apps.member.views',
    url(r'^$', 'view_login', {'login_template': 'login.html'}, name='login'),
)

