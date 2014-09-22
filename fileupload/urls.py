from django.conf.urls import patterns, url
from fileupload import views

urlpatterns = patterns('',
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^add/$', views.add_user, name='add_user'),
	url(r'^add/save/$', views.save_user, name='save_user'),
	url(r'^upload/$', views.upload_files, name='upload_files'),
	url(r'^uploaded/', views.uploaded_files, name='uploaded_files'),
	url(r'^upload/save/$', views.upload_files_saved, name='upload_files_saved'),
	url(r'^delete/(?P<file_id>\d+)/$', views.delete_file, name='delete'),
		)