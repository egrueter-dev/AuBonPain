from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hireapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'invite_registration.views.home_beta', name='home'),
    url(r'^home/beta/', 'invite_registration.views.home_beta', name='home_beta'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^beta/', include('invite_registration.urls')),

)
