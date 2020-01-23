from django.conf.urls import url
from django.urls import path

from api import views
from .views import AllTasks, CreateNewTask

urlpatterns = [
    path('', CreateNewTask.as_view()),
    path('alltasks/', AllTasks.as_view()),
    url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),# generate excel sheet on click
]
