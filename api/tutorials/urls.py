from django.conf.urls import url
from tutorials import views 
 
urlpatterns = [ 
    url(r'^service/new', views.create_service),
    url(r'^service/(?P<pk>\d+)$', views.service),
    url(r'^settings', views.settings),
    url(r'^breeds', views.breeds),
    url(r'^breed/(?P<pk>\d+)$', views.breed_detail),
    url(r'^tutors', views.tutors),
    url(r'^tutor/(?P<pk>\d+)$', views.tutor_detail),
    url(r'^schedule', views.schedule),
    url(r'^pets', views.pets),
    url(r'^tutor/new', views.create_tutor),
    url(r'^service_order', views.order),
    url(r'^service_order/(?P<pk>\d+)$', views.order_detail),
]
