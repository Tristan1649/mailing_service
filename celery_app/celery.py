import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailserv.settings')
# - Эта строка устанавливает переменную окружения 'DJANGO_SETTINGS_MODULE' для указания пути к файлу настроек Django вашего проекта "mailserv". 
# Это необходимо для того, чтобы Celery знал, какой файл настроек Django использовать.

app = Celery('mailserv')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailserv.settings') 


app.config_from_object('django.conf:settings', namespace='CELERY')
# Эта строка загружает настройки Celery из файла настроек Django. Она указывает, 
# что настройки Celery будут загружены из того же файла, который используется для загрузки настроек Django. 
# Параметр "namespace='CELERY'" говорит, что все настройки, связанные с Celery, будут начинаться с префикса "CELERY_".


app.autodiscover_tasks(['mailserv.celery_app'])
# Эта строка автоматически обнаруживает и загружает задачи Celery из файла "celery_app.py" внутри вашего проекта "mailserv". 
# В этом файле вы можете определить свои задачи Celery, которые будут выполняться асинхронно.
# В результате, после запуска этого кода, вы будете иметь настроенную и готовую к работе систему Celery, 
# которая будет работать вместе с вашим Django проектом "mailserv" и выполнять задачи асинхронно, например, отправку сообщений в фоновом режиме, 
# что позволит веб-приложению оставаться отзывчивым и быстрым.


