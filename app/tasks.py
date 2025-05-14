import time
from app.celery_app import celery
from celery import shared_task

@shared_task()
def background_task(message: str):
    time.sleep(10)
    print('Called')
    print(message)

