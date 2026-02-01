from src.enums.urls import Url


class TaskApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = Url.BASE_URL.value

    def create_task(self, task_data, list_id):
        # Отправляет запрос на создание task.
        response = self.auth_session.post(f"{self.base_url}/api/v2/list/{list_id}/task", json=task_data.model_dump())
        # Базовая проверка, что запрос успешен и можем парсить JSON.
        if response.status_code != 200:
            response.raise_for_status()  # Выбросит HTTPError для плохих статусов
        return response

    def get_task(self, task_id):
        # Отправляет запрос на получение task.
        response = self.auth_session.get(f"{self.base_url}/api/v2/task/{task_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response

    def delete_task(self, task_id):
        """Отправляет запрос на удаление task."""
        response = self.auth_session.delete(f"{self.base_url}/api/v2/task/{task_id}")
        if response.status_code != 204:  # В REST API для DELETE часто возвращают 204 No Content или 200 OK
            response.raise_for_status()
        # Для DELETE часто нечего возвращать из тела, либо можно вернуть статус-код или сам response
        return response  # или response.status_code
