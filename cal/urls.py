try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
    
urlpatterns = patterns(
    '',
    #URLs for acessing the basic profile information.
    url(r'^3year/$', 'cal.views.main', name = 'cal_this_main'),
    url(r'^3year/(\d+)/$', 'cal.views.main', name = 'cal_main'),
    
    url(r"^bymonth/(\d+)/(\d+)/$", 'cal.views.month', name = 'cal_month'),
    url(r"^bymonth/$", 'cal.views.month', name = 'cal_this_month'),
    
    url(r"^byday/(\d+)/(\d+)/(\d+)/$", 'cal.views.day', name = 'cal_day'),
    url(r"^today/$", 'cal.views.day', name = 'cal_today'),
    
    
)