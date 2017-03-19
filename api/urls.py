from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^user/$', views.UserList.as_view(), name=views.UserList.name),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name=views.UserDetail.name),
    url(r'^booking/$', views.BookingList.as_view(), name=views.BookingList.name),
    url(r'^booking/(?P<pk>[0-9]+)$', views.BookingDetail.as_view(), name=views.BookingDetail.name),
    url(r'^bus/$', views.BusList.as_view(), name=views.BusList.name),
    url(r'^bus/(?P<pk>[0-9]+)$', views.BusDetail.as_view(), name=views.BusDetail.name),
    url(r'^journey/$', views.RouteList.as_view(), name=views.RouteList.name),
    url(r'^journey/(?P<pk>[0-9]+)$', views.RouteDetail.as_view(), name=views.RouteDetail.name),
]

urlpatterns = format_suffix_patterns(urlpatterns)