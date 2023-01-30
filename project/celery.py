from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

import logging
from celery.signals import setup_logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')


# @setup_logging.connect
# def config_loggers(*args, **kwargs):
#     from logging.config import dictConfig  # noqa
#     from django.conf import settings  # noqa

#     dictConfig(settings.LOGGING)



# Tasks are stored in Tasks.py file
app.autodiscover_tasks()
