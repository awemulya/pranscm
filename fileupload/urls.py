from django.conf.urls import patterns, url
from fileupload import views

urlpatterns = patterns('',
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^add/$', views.add_user, name='add_user'),
	url(r'^add/save/$', views.save_user, name='save_user'),
		)