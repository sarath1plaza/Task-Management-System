from django.urls import path,include
from Task_app_1 import views
from .views import Task_dataListView

urlpatterns = [
    path('',Task_dataListView.as_view(),name='home'),
    path('all_tasks/',views.All_tasks),
    path('api/auth/', include('djoser.urls.authtoken')),
]
