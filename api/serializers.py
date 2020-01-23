from rest_framework import serializers
from Task_app_1.models import Task_data


class TaskDataSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'employee_name', 'task', 'deadline', 'status', 'task_assign_time')
        model = Task_data

