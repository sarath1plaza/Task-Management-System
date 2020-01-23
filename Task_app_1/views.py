from django.shortcuts import render
from django.http import HttpResponse
from Task_app_1.models import *
from django.views.generic import ListView
from .models import Task_data


def login(request):
    if request.method == 'POST':
        user = request.POST.get('mail')
        pswd1 = request.POST.get('password')
        if employee.objects.all().filter(User_id=user).filter(Password=pswd1).exists():
            request.session['mail'] = user
            return HttpResponse('Login')
        else:
            return render(request, 'Login.html', {'msg': 'Invalid username or password'})
    return render(request,'Login.html')


def All_tasks(request):
    ob=Task_data.objects.raw("select * from Task_app_1_task_data order by id  desc ")
    return render(request, 'All_tasks.html',context={'data':ob})


class Task_dataListView(ListView):
    model = Task_data
    template_name = 'books/book_list.html'
