from django.urls import path, include
from rest_framework import permissions
from .views import ClientListCreateView, CampaignListCreateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from . import campaign_views, statistics_views
from . import views

#Генерирует OpenAPI-спецификацию API с помощью DRF YASG.
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentation for your API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True, # Делает документацию публично доступной.
    permission_classes=(permissions.AllowAny,), #Разрешает доступ без аутентификации.
)

urlpatterns = [
    #Здесь используется библиотека DRF YASG для создания документации API в формате Swagger UI. 
    # Пользователи могут просматривать документацию API, 
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    #маршрут связан с представлением ClientListCreateView, 
    # которое обрабатывает запросы на создание (POST) и получение списка (GET) клиентов
    path('api/clients/', ClientListCreateView.as_view(), name='client-list-create'),
    
    
    #маршрут связан с представлением CampaignListCreateView, которое 
    # обрабатывает запросы на создание (POST) и получение списка (GET) кампаний.
    path('api/campaigns/', CampaignListCreateView.as_view(), name='campaign-list-create'),
    
    
    #еще одна возможность просмотра документации API с использованием библиотеки DRF YASG, 
    # но в более компактном и красивом формате ReDoc.
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # маршрут используется для получения 
    # JWT-токена аутентификации с помощью представления TokenObtainPairView.
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
       
    
    # маршрут используется 
    # для обновления JWT-токена с помощью представления TokenRefreshView.
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]