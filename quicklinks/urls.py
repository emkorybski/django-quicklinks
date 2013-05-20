from django.conf.urls import patterns, include, url
from django.conf import settings
from quicklinks import views



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'quicklinks.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^links/$', 'quicklinks.views.links', name='links'),
    url(r'^groupedlinks/$', 'quicklinks.views.groupedlinks', name='groupedlinks'),
    url(r'^$', 'quicklinks.views.home', name='default'),
    url(r'^index/$', 'quicklinks.views.index', name='index'),
    #url(r'^index/l/$', views.index.groups_list, name='list'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^%s(?P<path>.*)$' % (settings.MEDIA_URL[1:],), 'serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True }),)