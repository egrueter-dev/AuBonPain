from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hireapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'invite_registration.views.home_beta', name='home'),
    url(r'^home/beta/', 'invite_registration.views.home_beta', name='home_beta'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^beta/', include('invite_registration.urls')),

)
