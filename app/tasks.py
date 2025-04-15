import time
from app.celery_app import celery


@celery.task
def background_task(message: str):
    time.sleep(10)
    print('Called')
    print(message)

