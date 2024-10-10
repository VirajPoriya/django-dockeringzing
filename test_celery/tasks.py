from celery import shared_task
import time
from test_celery.models import TestCeleryModel

@shared_task
def test_celery():
    obj = TestCeleryModel.objects.create(
        text="test",
        description="ksvk",

    )
    time.sleep(10)  # Simulating a long-running task
    obj.is_completed = True
    obj.save()
    


