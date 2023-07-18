from django.apps import AppConfig


class ServiceConfig(AppConfig):
    # ServiceConfig - класс настройки приложения service в Django.
    
    default_auto_field = 'django.db.models.BigAutoField'
    # default_auto_field = 'django.db.models.BigAutoField': 
    # Указывает на использование BigAutoField для автоинкрементного поля (primary key) моделей приложения.
    
    name = 'service' 
    # name = 'service': Задает имя вашего приложения, которое должно быть 'service'.





