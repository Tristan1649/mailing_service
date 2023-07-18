from rest_framework import serializers
from .models import Client, Campaign, Message

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
# Каждый сериализатор определен с помощью класса serializers.ModelSerializer. 
# Поля, которые будут включены в сериализацию, указываются в fields = '__all__', 
# что означает, что будут использованы все поля модели. 
# Это позволяет автоматически создать 
# JSON-представления для объектов моделей Client, Campaign и Message.