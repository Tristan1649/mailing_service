from django.db import models

class Client(models.Model):
    phone_number = models.CharField(max_length=12) #Номер телефона клиента 
    mobile_operator_code = models.CharField(max_length=10) #Код мобильного оператора
    tag = models.CharField(max_length=255) #Тег клиента
    timezone = models.CharField(max_length=255) #Часовой пояс клиента

class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #Дата и время создания сообщения (DateTimeField, 
                                                         # автоматически заполняется при создании)
    status = models.CharField(max_length=255)  # Статус сообщения
    client = models.ForeignKey(Client, on_delete=models.CASCADE) #Внешний ключ (ForeignKey) на модель Client

class Campaign(models.Model):  #Модель Django, представляющая рассылку (кампанию)
    start_time = models.DateTimeField() #Дата и время начала рассылки 
    end_time = models.DateTimeField() # Дата и время окончания рассылки
    message = models.TextField() # Текст сообщения
    client_filter = models.CharField(max_length=255) #Текст сообщения
    message = models.ForeignKey( 
        Message, related_name='campaigns', on_delete=models.CASCADE 
        #Внешний ключ (ForeignKey) на модель Message
    )

