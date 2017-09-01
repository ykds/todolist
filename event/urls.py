from django.conf.urls import url
from . import views


app_name = 'event'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventView.as_view(), name='events'),
    url(r'^events/done/(?P<event_pk>[0-9]+)/$', views.done, name='done'),
    url(r'^events/delete/(?P<event_pk>[0-9]+)/$', views.delete, name='delete'),
    url(r'^events/info/(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='info'),
    url(r'^events/post/(?P<user_pk>[0-9]+)/$', views.post_plan, name='add'),
]