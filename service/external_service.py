import requests

# APIClient: Класс 
# для отправки сообщений на внешний сервис через API 
# с аутентификацией по JWT токену.
class APIClient:
    def __init__(self):
        self.base_url = 'https://probe.fbrq.cloud'
        self.access_token = None

    def authenticate(self, jwt_token):
        self.access_token = jwt_token

    def send_message(self, message):
        if not self.access_token:
            raise Exception('Authentication required. Please authenticate using the authenticate() method.')

        url = f'{self.base_url}/send/sendMsg'
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {'message': message}

        try:
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f'Error sending message. Status code: {response.status_code}')
        except requests.RequestException as e:
            raise Exception(f'Error sending message: {str(e)}')

def send_message_to_external_service(message): 
    # send_message_to_external_service: Функция для отправки 
    # сообщения с использованием APIClient и обработки ответа.

    
    api_client = APIClient()

    try:
        # Аутентификация с помощью токена доступа JWT
        api_client.authenticate('your_jwt_token')

        # Вызов метода API для отправки сообщения
        response = api_client.send_message(message)

        # Обработка ответа
        if response['success']:
            # Сообщение успешно отправлено
            # Можно выполнить дополнительные действия или обновить статус сообщения в базе данных
            pass
        else:
            # Обработка ошибки external_service
            # Можно выполнить дополнительные действия или записать информацию об ошибке в логи
            pass
    except Exception as e:
        # Обработка других ошибок, например, проблем с соединением или некорректным форматом данных
        # Можно выполнить дополнительные действия или записать информацию об ошибке в логи
        pass
