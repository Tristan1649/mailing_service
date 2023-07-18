from rest_framework import generics
from .models import Client, Campaign, Message
from .serializers import ClientSerializer, CampaignSerializer, MessageSerializer
from django.utils import timezone


#позволяет получать список клиентов (GET) и создавать новых клиентов (POST).
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



#позволяет получать, обновлять и удалять данные конкретного клиента.
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer




#позволяет получать, обновлять и удалять данные конкретного клиента.
class CampaignListCreateView(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

#  позволяет получать, обновлять и удалять данные конкретной кампании.
class CampaignDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    
#  позволяет получать, обновлять и удалять данные конкретной кампании.
class CampaignStatisticsView(generics.RetrieveAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

# позволяет получать, обновлять и удалять данные конкретного клиента.
class MessageDetailView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# позволяет получать, обновлять и удалять данные конкретного клиента.
class ActiveCampaignsProcessingView(generics.ListAPIView):
    queryset = Campaign.objects.filter(end_time__gte=timezone.now())
    serializer_class = CampaignSerializer


