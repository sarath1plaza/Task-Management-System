import csv
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.jobstores import register_events
from django.utils import timezone
from Task_app_1.models import Task_data

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
register_events(scheduler)

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

#code for autogenerate task details included excel sheet on weekely basis

@register_job(scheduler, "interval", weeks=1)
def test_job():
    filename = str(timezone.now())
    with open('./exports/' + filename + '.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Task No', 'Employee name', 'Tasks', 'Assign date', 'Dead line', 'Current status'])
        users = Task_data.objects.all().values_list('id', 'employee_name', 'task', 'task_assign_time', 'deadline',
                                                    'status')
        for user in users:
            writer.writerow(user)
    print("Successfully created new document", filename)
    return


register_events(scheduler)
scheduler.start()

