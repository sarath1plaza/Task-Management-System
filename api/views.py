import csv
from apiview.view import APIView
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from Task_app_1.models import Task_data
from .serializers import TaskDataSerializer
from api import excelScheduler
from api import *

import django.utils.timezone

dt = django.utils.timezone.now()


class CreateNewTask(generics.ListCreateAPIView):
    queryset = Task_data.objects.all()
    serializer_class = TaskDataSerializer


class AllTasks(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks.html'

    def get(self, request):
        queryset = Task_data.objects.raw("select * from Task_app_1_task_data order by id  desc ")
        return Response({'data': queryset})


def export_users_csv(response):
    print("I'm a test job!")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="weekely_basis_task.csv"'

    writer = csv.writer(response)
    writer.writerow(['No', 'Employee name', 'Assign date', 'Dead line', 'Current status'])

    users = Task_data.objects.all().values_list('id', 'employee_name', 'task_assign_time', 'deadline', 'status')
    for user in users:
        writer.writerow(user)
    return response
