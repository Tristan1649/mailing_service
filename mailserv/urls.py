from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Путь к административной панели
    path('admin/', admin.site.urls),
    
    # Включаем URL-шаблоны из приложения "service"
    path('', include('service.urls')),
]
