from django.contrib import admin
from django.conf.urls import patterns, url, include
import cauth.views
from cauth.urls import patterns, url

urlpatterns = patterns('',
  url(r'login/$', cauth.views.login),
  url(r'auth/$', cauth.views.auth_view),
  url(r'logout/$', cauth.views.logout),
  url(r'loggedin/$', cauth.views.loggedin),
  url(r'invalid/$', cauth.views.invalid_login),
  url(r'register/$', cauth.views.register),
  url(r'register_success/$', cauth.views.register_success),
  url(r'edit/$', cauth.views.edit),
  url(r'password/$', cauth.views.password),
)