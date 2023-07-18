from django.contrib import admin
from .models import Client, Campaign, Message


# Регистрирует модели в административной панели Django.
# После регистрации в административной панели будет доступна страница управления клиентами, 
# где можно просматривать, добавлять, редактировать и удалять клиентов.

admin.site.register(Client)
admin.site.register(Campaign)
admin.site.register(Message)
