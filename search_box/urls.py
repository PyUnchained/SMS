from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^testing/$',
    	'search_box.views.testing', name = 'testing'),

    url(r'^testing/(?P<action>\w+)/(?P<obj_pair>\w+)/$',
        'search_box.views.testing', name = 'testing'),

    url(r'^search/$', 'search_box.views.search',
    	name = 'search_box_search'),

    url(r'^sa/$', 'search_box.views.search_actions',
    	name = 'search_actions'),



)
