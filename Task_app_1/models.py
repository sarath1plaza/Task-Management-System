from django.db import models
from django.utils import timezone


class Task_data(models.Model):
    employee_name = models.CharField(max_length=50)
    task = models.CharField(max_length=500)
    deadline = models.DateTimeField()
    task_assign_time=models.DateTimeField(default=timezone.now,editable=False)
    status = models.CharField(max_length=50,default='Not completed')

