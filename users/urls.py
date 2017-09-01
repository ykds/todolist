from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns =[
    url(r'users/register/$', views.register, name='register'),
    url(r'users/profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'users/edit/(?P<pk>[0-9]+)/$', views.ProfilEditView.as_view(), name='edit'),
]