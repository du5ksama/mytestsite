from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tasknote_list, name='tasknote_list'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^note/new/$', views.note_new, name='note_new'),
]
