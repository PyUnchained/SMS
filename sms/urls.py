from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	#For logging in
	url(r'^$', 'sms.views.login', name = 'login'),
	url(r'^logout/', 'sms.views.logout', name = 'logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sysadmin/', include('sms_admin.urls')),
    url(r'^msg/', include('msg_box.urls')),
    url(r'^office/', include('office.urls')),
    url(r'^cal/', include('cal.urls')),
    url(r'^search/', include('search_box.urls')),
)

#These lines of code are needed for the django development server to serve media files.
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )