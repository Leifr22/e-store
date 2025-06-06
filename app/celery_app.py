from celery import Celery

celery=Celery(
    __name__,
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    broker_connection_retry_on_startup=True
)

celery.autodiscover_tasks(['app'])