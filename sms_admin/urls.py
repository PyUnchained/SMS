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

    url(r'^class_details/(?P<pk>\d+)/$',
        'sms_admin.views.class_details', name = 'class_details'),

    url(r'^class_details/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.class_details', name = 'class_details'),

    url(r'^classes/$',
        'sms_admin.views.all_classes', name = 'all_classes'),

    url(r'^classes/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.all_classes', name = 'all_classes'),

    url(r'^ajax-add-student-to-class/$',
        'office.views.PersonToClass', name = 'add_person_to_class'),

    url(r'^courses/$',
        'sms_admin.views.all_courses', name = 'all_courses'),

    url(r'^courses/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.all_courses', name = 'all_courses'),

    url(r'^course_details/(?P<pk>\d+)/$',
        'sms_admin.views.course_details', name = 'course_details'),

    url(r'^course_details/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.course_details', name = 'course_details'),


)
