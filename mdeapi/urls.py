from django.conf.urls import patterns, include, url
from api.views import parkHours, itineraryForDate

urlpatterns = patterns('',
    url(r'^hours/(?P<year>\d{4})/(?P<month>\d{2})/(?P<date>\d+)/$', parkHours),
    url(r'^date/(?P<year>\d{4})/(?P<month>\d{2})/(?P<date>\d+)/$', itineraryForDate),
)
