from django.contrib.auth.models import Group
from django.contrib import admin

# code for Django admin panel cutomization

admin.site.site_header = 'Task Management System'
admin.site.site_title = 'Task Management System'
admin.site.unregister(Group)