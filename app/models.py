from django.db import models

# Create your models here.
'''
Data to log:
● celery task ID
● status of the celery task (Success, failed, pending, running, etc)
● arguments used to run the job (ie: filename and the data count))
'''

class Celery_log(models.Model):
    task_id = models.UUIDField(editable=False, unique=True)
    status = models.CharField(max_length=20)
    arguments = models.JSONField(max_length=50)

    class Meta:
        ordering = ["-id"]

    def __str__(self) -> str:
        return str(self.arguments)