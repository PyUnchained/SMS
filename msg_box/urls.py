from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^inbox/$', 'msg_box.views.inbox', name = 'msg_box_inbox'),
    url(r'^sentbox/$', 'msg_box.views.sentbox', name = 'msg_box_sentbox'),
    url(r'^trashbox/$', 'msg_box.views.trashbox', name = 'msg_box_trashbox'),
    url(r'^compose/$', 'msg_box.views.compose', name = 'msg_box_compose'),
    url(r'^compose/(\w+)/$', 'msg_box.views.compose', name = 'msg_box_reply'),
    url(r'^compose/(\w+)/(\w+)/$', 'msg_box.views.compose', name = 'msg_box_forward'),
    url(r'^view/(\d+)/$', 'msg_box.views.view_message', name = 'msg_box_view'),
    url(r'^del/(\d+)/$', 'msg_box.views.delete_message', name = 'msg_box_delete'),

)
