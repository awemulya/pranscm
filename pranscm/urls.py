from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib import admin
from django.contrib.auth import views
from fileupload import views as file_upload_view
# from django.views.generic.base import TemplateView

# admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
	# url(r'', include('django.contrib.auth.urls')),
	url(r'^$',file_upload_view.dashboard , name='dashboard'),
	url(r'^dashboard/$',file_upload_view.dashboard , name='dashboard'),
	url(r'^login/$', views.login, {'template_name': 'registration/login.html'}, name='login'),
	url(r'^logout/$', views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
	url(r'^password_change/$', views.password_change, {'template_name': 'registration/password_change_form.html'}, name='password_change'),
	url(r'^password_change/done/$', views.password_change_done, {'template_name': 'registration/password_change_done.html'}, name='password_change_done'),
	# url(r'^admin/', include(admin.site.urls)),
	) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)