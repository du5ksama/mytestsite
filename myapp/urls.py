from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tasknote_list, name='tasknote_list'),
]
