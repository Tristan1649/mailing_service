Документация API 
Сервиса управления рассылками


Добро пожаловать в документацию API Сервиса управления рассылками для проекта "mailserv" и приложения "service". 
Этот API позволяет создавать, управлять и отправлять уведомления клиентам. 
API разработан с использованием Django и Django REST Framework, 
использует Python 3.11.4 и интегрируется с внешним сервисом, который принимает запросы на отправку сообщений в сторону клиентов.

Примененные библиотеки:
Django - фреймворк для разработки веб-приложений на языке Python.
Django REST Framework - расширение Django для создания RESTful API.
Celery - библиотека для асинхронной обработки задач.
Redis - система хранения данных в памяти для использования в качестве брокера сообщений для Celery.
Django Simple JWT - библиотека для обеспечения аутентификации с использованием JSON Web Tokens (JWT).
drf-yasg - инструмент для генерации документации API на основе Django REST Framework.
requests - библиотека для выполнения HTTP-запросов к внешнему сервису отправки сообщений.
unittest - библиотека для создания и запуска тестов.


Аутентификация
Для доступа к API требуется аутентификация с использованием токена доступа JWT (JSON Web Token). 
Все эндпоинты, кроме получения токена, 
требуют наличия токена в заголовке запроса. Чтобы получить токен доступа, вы можете использовать эндпоинт:

Получение токена доступа
URL: /token/
Метод: POST


Параметры запроса:
username (строка) - Имя пользователя для аутентификации.
password (строка) - Пароль для аутентификации.
Пример запроса:
POST /token/
{
  "username": "your_username",
  "password": "your_password"
}

Пример ответа:
json
Copy code
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}

Эндпоинты API
Клиенты
Создание нового клиента
URL: /api/clients/
Метод: POST
Аутентификация: требуется JWT токен доступа.
Параметры запроса:

phone_number (строка) - Номер телефона клиента.
mobile_operator_code (строка) - Код мобильного оператора клиента.
tag (строка) - Тег клиента.
timezone (строка) - Часовой пояс клиента.

Пример запроса:
bash
Copy code
POST /api/clients/
{
  "phone_number": "1234567890",
  "mobile_operator_code": "XYZ",
  "tag": "new_client",
  "timezone": "Europe/London"
}

Пример ответа:

json
Copy code
{
  "id": 1,
  "phone_number": "1234567890",
  "mobile_operator_code": "XYZ",
  "tag": "new_client",
  "timezone": "Europe/London"
}
Получение списка клиентов
URL: /api/clients/
Метод: GET
Аутентификация: требуется JWT токен доступа.

Пример ответа:
css
Copy code

Пример ответа:
css
Copy code
[{"id": 1, 
"phone_number": "1234567890",  
"mobile_operator_code": "XYZ", 
"tag": "new_client", 
"timezone": "Europe/London"},  

{"id": 2,  
"phone_number": "9876543210", 
 "mobile_operator_code": "ABC",  
"tag": "existing_client", 
"timezone": "America/New_York"}]


Рассылки
Создание новой рассылки

URL: /api/campaigns/
Метод: POST

Аутентификация: требуется JWT токен доступа.

Параметры запроса:

start_time (строка) - Время начала рассылки.
end_time (строка) - Время окончания рассылки.
message (строка) - Содержание сообщения для рассылки.
client_filter (строка) - Фильтр для выбора клиентов для рассылки.

Продолжение документации API Сервиса управления рассылками:

Пример запроса:
bash
Copy code
POST /api/campaigns/
{
  "start_time": "2023-07-18 10:00:00",
  "end_time": "2023-07-20 18:00:00",
  "message": "Здравствуйте! Это уведомление для вас.",
  "client_filter": "new_client"
}

Пример ответа:

json
Copy code
{
  "id": 1,
  "start_time": "2023-07-18 10:00:00",
  "end_time": "2023-07-20 18:00:00",
  "message": "Здравствуйте! Это уведомление для вас.",
  "client_filter": "new_client"
}

Получение списка рассылок
URL: /api/campaigns/
Метод: GET
Аутентификация: требуется JWT токен доступа.

Пример ответа:

css
Copy code
[{"id": 1, 
"start_time": "2023-07-18 10:00:00", 
"end_time": "2023-07-20 18:00:00", 
"message": "Здравствуйте! Это уведомление для вас.", "client_filter": "new_client"  },  

{"id": 2, 
"start_time": "2023-07-19 12:00:00", 
"end_time": "2023-07-22 20:00:00",  
"message": "Спасибо за использование нашего сервиса!", 
"client_filter": "existing_client"  }]





Статистика
Получение статистики рассылки
URL: /api/campaigns/<campaign_id>/statistics/
Метод: GET
Аутентификация: требуется JWT токен доступа.
Параметры запроса:

campaign_id (число) - Идентификатор рассылки для получения статистики.

Пример запроса:

bash
Copy code
GET /api/campaigns/1/statistics/
Пример ответа:

json
Copy code
{
  "total_messages": 100,
  "sent_messages": 90,
  "failed_messages": 10
}

Интеграция с внешним сервисом
Данный API взаимодействует с внешним сервисом для отправки уведомлений клиентам. 
Внешний сервис доступен по адресу https://probe.fbrq.cloud/docs. 
Взаимодействие с внешним сервисом происходит через аутентификацию с использованием токена доступа JWT, 
который предоставлен вам вместе с тестовым заданием.

Документация Swagger UI
Для просмотра документации API и взаимодействия с ним используйте Swagger UI. Он доступен по адресу /docs/. 
Здесь вы можете изучить все эндпоинты, отправлять запросы, а также просматривать параметры и ответы для каждого эндпоинта.

Пример: Swagger UI

Заключение
Это документация API Сервиса управления рассылками. 
API предоставляет инструменты для управления рассылками и клиентами, 
а также интегрирован с внешним сервисом для отправки уведомлений. 
Пользуйтесь этим API с удовольствием!