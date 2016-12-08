from django.conf.urls import url
from intro.views import *

urlpatterns = [
	url(r'^index/(?P<teamId>\d+)/$', index, name='index'),
	url(r'^detail/(?P<memberId>\d+)/$', detail, name='detail'),
	url(r'^top$', top, name='top'),

]
