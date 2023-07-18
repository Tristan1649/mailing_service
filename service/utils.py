from django.core.mail import send_mail
from .models import Client, Campaign, Message


#Отправляет сообщение по электронной почте на указанный адрес. 
# Если отправка успешна, обновляет статус сообщения на "sent", в противном 
# случае устанавливает статус "failed" и сохраняет ошибку.
def send_email(message):
    # Логика отправки сообщения по электронной почте
    try:
        send_mail(
            message.subject,
            message.body,
            'sender@example.com',
            [message.recipient_email],
            fail_silently=False,
        )
        message.status = 'sent'
        message.save()
    except Exception as e:
        message.status = 'failed'
        message.error_message = str(e)
        message.save()



# Обрабатывает рассылку, создавая сообщения для каждого клиента, 
# устанавливает статус "pending" и отправляет каждое 
# сообщение по электронной почте с помощью функции send_email.
def process_campaign(campaign):
    # Логика обработки рассылки
    clients = Client.objects.filter(some_filter=campaign.filter)
    for client in clients:
        message = Message(
            campaign=campaign,
            client=client,
            recipient_email=client.email,
            subject=campaign.subject,
            body=campaign.body,
            status='pending',
        )
        message.save()
        send_email(message)
