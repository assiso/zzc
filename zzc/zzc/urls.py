from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zzc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^adam2014/',include('adam2014.urls',namespace="adam2014")),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
) 

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf goes here ...

urlpatterns += staticfiles_urlpatterns()