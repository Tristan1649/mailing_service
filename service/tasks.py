from celery import shared_task
from .models import Campaign, Message, Client
from .utils import send_email


#process_campaign: Задача Celery для обработки рассылки кампании. Создает сообщения 
# для клиентов и отправляет на асинхронную обработку send_message.
@shared_task
def process_campaign(campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
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
        send_message.delay(message.id)


# send_message: Задача Celery для отправки сообщений. 
# Отправляет сообщения и обновляет их статус в базе данных.
@shared_task
def send_message(message_id):
    message = Message.objects.get(id=message_id)
    try:
        send_email(message)
        message.status = 'sent'
    except Exception as e:
        message.status = 'failed'
        message.error_message = str(e)
    message.save()
