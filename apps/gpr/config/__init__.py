from __future__ import absolute_import, unicode_literals

# Esto hace que la aplicación Celery sea accesible desde cualquier lugar
from .celery import app as celery_app

__all__ = ('celery_app',)
