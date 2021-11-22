from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^service/(?P<pk>\d+)$', views.service),
    url(r'^settings', views.settings),
    url(r'^breeds', views.breeds),
    url(r'^breed/(?P<pk>\d+)$', views.breed_detail),
    url(r'^tutors', views.tutors),
    url(r'^tutor/(?P<pk>\d+)$', views.tutor_detail),
    url(r'^schedule', views.schedule),
]
