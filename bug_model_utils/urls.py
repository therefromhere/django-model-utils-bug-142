from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bug_model_utils.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^bug/', include('bug.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
