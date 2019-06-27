from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^place', views.placePut),

]
