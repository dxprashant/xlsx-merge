from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse

urlpatterns = patterns('',

    url(r'^$', 'uploader.views.list', name='list'),
    url(r'^download/(?P<file_name>.+)$', 'joints.views.download'),
    (r'^',include('joints.urls')),
    (r'^',include('workbook.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
