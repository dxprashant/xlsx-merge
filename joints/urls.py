#self created
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from joints import views


urlpatterns = patterns('joints.views',
    url(r'^home/$', 'home', name='home'),
)
