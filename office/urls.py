from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^search/$', 'office.views.search', name = 'search'),
	url(r'^search/(?P<pk>\w+)/$', 'office.views.search', name = 'search'),
)