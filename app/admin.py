from django.contrib import admin
from .models import Celery_log

# Register your models here.

class CeleryLogAdmin(admin.ModelAdmin):
    list_display = ["task_id", "status", "arguments"]

admin.site.register(Celery_log, CeleryLogAdmin)