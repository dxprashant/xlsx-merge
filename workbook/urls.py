#self created
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from joints import views


urlpatterns = patterns('workbook.views',
    url(r'^wb/$', 'home', name='wb'),
    #url(r'^wbdownload/$', 'home', name='wb'),
    
)
