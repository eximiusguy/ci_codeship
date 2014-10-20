from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ci_codeship.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register$', 'employee.views.employee_registration', name='register'),
    url(r'^employee-list$', 'employee.views.employee_listing', name='employee_list'),

    url(r'^admin/', include(admin.site.urls)),
)
