from django.shortcuts import render
from .tasks import generate_file
from .models import Celery_log

# Create your views here.

'''
Data to log:
● celery task ID
● status of the celery task (Success, failed, pending, running, etc)
● arguments used to run the job (ie: filename and the data count))
'''
import time

def index(request):
    if request.method == "POST":
        file_name = request.POST.get('fileName')
        rows = request.POST.get('rows')
        

        try:
            task=generate_file.delay(file_name, rows)
            task_id = task.id
            
        except:
            pass
        finally:
            time.sleep(0.5)
            result = generate_file.AsyncResult(task_id)
            
            Celery_log.objects.create(task_id=task_id, status=result.status, arguments={"filename": file_name, "rows": rows})
        return render(request, 'success.html')
    return render(request, 'index.html')

