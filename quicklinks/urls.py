try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'quicklinks.views.home', name='home'),
    url(r'^quicklinks/$', 'quicklinks.views.links', name='links'),
    url(r'^index/$', 'quicklinks.views.indexAlt', name='index'),
)
