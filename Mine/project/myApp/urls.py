from django.conf.urls import url
from myApp import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^send/$', views.sendMail),

    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle/$', views.session2_handle),
    url(r'^session3/$', views.session3),

]

