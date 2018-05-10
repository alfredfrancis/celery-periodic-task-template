from datetime import timedelta

from celery import Celery
from celery.task import periodic_task


"""
Intialize celery worker with redis as message broker
message broker is used here to persist informations \
for the worker such any status updates,running times,results etc
"""
app = Celery('tasks', broker='redis://localhost:6379/0')


"""
a celery periodic function.
This will executed as per the scheduled times
eg: run_every=timedelta(seconds=5) will make it run every min

ref: http://docs.celeryproject.org/en/latest/reference/celery.schedules.html
ref: http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
"""
@periodic_task(run_every=timedelta(seconds=5))
def sample_function():
    # add your periodic code here
    return ' i running periodic task '