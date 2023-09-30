import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Python_Test_Task_HQ.settings')

application = get_wsgi_application()
