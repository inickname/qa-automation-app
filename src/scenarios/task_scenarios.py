from src.api_clients.task_api_client import TaskApiClient
from src.data_models.task_response_data_model import TaskResponseModel
from src.utils.validate_task_response import ValidateTaskResponse
from tests.conftest import task_data, delete_manager


class TaskScenarios:
    def __init__(self, api_client: TaskApiClient):  # Типизация для ясности
        self.api_client = api_client

    def create_task_and_check(self, delete_manager, task_data, list_id):
        """
        Сценарий: создать и проверить task.
        Возвращает ID созданного task.
        """
        task_data = task_data()
        created_task_data = self.api_client.create_task(task_data, list_id)
        task_id = created_task_data.json().get("id")
        assert task_id is not None, f"ID не найден в ответе на создание: {created_task_data}"

        ValidateTaskResponse.validate_response(created_task_data, TaskResponseModel, 200,
                                               task_data.model_dump())

        print(f"Task с ID {task_id} успешно создан.")
        delete_manager.append(task_id)
        return task_id

    def get_and_verify_task_exist(self, task_id):
        """
        Сценарий: получить task и проверить, что ответ не пуст.
        """
        task = self.api_client.get_task(task_id).json()

        assert task, "Ответ task пуст"
        print(f"Получена информация о task с id '86c7f4v8a'.")

        return task
