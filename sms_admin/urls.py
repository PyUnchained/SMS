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

    url(r'^view_students/(\d+)/$',
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

    url(r'^classes/(?P<action>\w+)/(?P<course_pk>\d+)/$',
        'sms_admin.views.all_classes', name = 'all_classes'),

    url(r'^classes/(?P<action>\w+)/(?P<pk>\d+)/(?P<student_pk>\d+)/$',
        'sms_admin.views.all_classes', name = 'all_classes'),

    url(r'^ajax-add-student-to-class/$',
        'office.views.PersonToClass', name = 'add_person_to_class'),

    url(r'^courses/$',
        'sms_admin.views.all_courses', name = 'all_courses'),

    url(r'^courses/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.all_courses', name = 'all_courses'),

    url(r'^courses/(?P<action>\w+)/(?P<pk>\d+)/(?P<subject_pk>\d+)/$',
        'sms_admin.views.all_courses', name = 'all_courses'),

    url(r'^course_details/(?P<pk>\d+)/$',
        'sms_admin.views.course_details', name = 'course_details'),

    url(r'^course_details/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.course_details', name = 'course_details'),

    url(r'^ajax-add-subject-to-course/$',
        'office.views.SubjectToCourse', name = 'add_subject_to_course'),

    url(r'^ajax-add-course-to-campus/$',
        'office.views.CourseToCampus', name = 'add_course_to_campus'),

    url(r'^subjects/$',
        'sms_admin.views.all_subjects', name = 'all_subjects'),

    url(r'^subjects/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.all_subjects', name = 'all_subjects'),

    url(r'^subject_details/(?P<pk>\d+)/$',
        'sms_admin.views.subject_details', name = 'subject_details'),

    url(r'^subject_details/(?P<action>\w+)/(?P<pk>\d+)/$',
        'sms_admin.views.subject_details', name = 'subject_details'),


)
