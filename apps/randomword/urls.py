from django.conf.urls import url
from . import views
app_name = 'randomword'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generate$', views.generate, name='generate'),
]