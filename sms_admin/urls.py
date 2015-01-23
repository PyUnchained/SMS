from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/$', 'sms_admin.views.home', name = 'sysadmin_home'),

    url(r'^view_students/$',
    	'sms_admin.views.view_students', name = 'view_students'),

    url(r'^view_students/(\w+)/$',
    	'sms_admin.views.view_students', name = 'view_one_student'),

    url(r'^student_classes/(\w+)/$',
    	'sms_admin.views.view_classes', name = 'view_student_classes'),

    url(r'^student_classes/(\w+)/(\w+)/$',
        'sms_admin.views.view_classes', name = 'view_student_classes'),

    url(r'^class_details/(\w+)/$',
        'sms_admin.views.class_details', name = 'class_details'),

    url(r'^class_details/(\w+\s+\w+)/$',
        'sms_admin.views.class_details', name = 'class_details'),


)
