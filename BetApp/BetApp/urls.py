from django.contrib import admin
from django.conf.urls import patterns, url, include
from cauth.urls import patterns, url
import cauth.views
import BetApp.views 

urlpatterns = patterns('',
  (r'^$', BetApp.views.index),
  (r'^admin/', admin.site.urls),
  (r'^account/', include(cauth.urls)),
  (r'^balance/$', BetApp.views.balance),
  (r'^bet/$', BetApp.views.bet),
  # ...
)
