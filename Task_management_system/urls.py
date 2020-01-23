from django.contrib import admin
from django.urls import path,include

from Task_app_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # path('tasks/',views.All_tasks),
    path('api/',include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
]

