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
        task_data = task_data().model_dump()
        created_task_data = self.api_client.create_task(task_data, list_id)

        task_id = created_task_data.json().get("id")
        assert task_id is not None, f"ID не найден в ответе на создание: {created_task_data}"

        ValidateTaskResponse.validate_response(created_task_data, TaskResponseModel, 200,
                                               task_data)

        print(f"Task с ID {task_id} успешно создан.")
        delete_manager.append(task_id)
        return task_id

    def get_and_verify_task_exist(self, delete_manager, task_data, list_id):
        """
        Сценарий: получить task и проверить, что ответ не пуст.
        """
        task_data = task_data().model_dump()
        task_id = self.api_client.create_task(task_data, list_id).json().get("id")

        gotten_task_data = self.api_client.get_task(task_id)
        assert gotten_task_data.json(), "Ответ task пуст"

        ValidateTaskResponse.validate_response(gotten_task_data, TaskResponseModel, 200, task_data)
        print(f"Получена информация о task с id {task_id}.")
        delete_manager.append(task_id)
        return task_id

    def update_task_and_check(self, delete_manager, task_data, list_id):
        """
        Сценарий: создать, изменить и проверить task.
        Возвращает ID измененного task.
        """
        task_data_1 = task_data().model_dump()
        task_data_2 = task_data().model_dump()
        task_id = self.api_client.create_task(task_data_1, list_id).json().get("id")

        updated_task_data = self.api_client.update_task(task_id, task_data_2)

        task_id = updated_task_data.json().get("id")
        assert task_id is not None, f"ID не найден в ответе на изменение: {updated_task_data}"

        ValidateTaskResponse.validate_response(updated_task_data, TaskResponseModel, 200,
                                               task_data_2)

        print(f"Task с ID {task_id} успешно изменен.")
        delete_manager.append(task_id)
        return task_id

    def delete_existing_task_and_verify(self, task_data, list_id):
        """
        Сценарий: создать и удалить task.
        Возвращает статус-код.
        """
        task_data = task_data().model_dump()
        task_id = self.api_client.create_task(task_data, list_id).json().get("id")

        deleted_task_data = self.api_client.delete_task(task_id)
        print(f"Task с ID {task_id} отправлен на удаление.")
        return deleted_task_data.status_code

    def create_task_negative(self, invalid_task_data, list_id, expected_status_code):
        """
        Сценарий: создать task с разными наборами невалидных данных,
        чтобы убедиться, что система правильно обрабатывает ошибки.
        """
        response = self.api_client.create_task(invalid_task_data, list_id, expected_status_code)

        assert response.status_code == expected_status_code, (f"Ожидался {expected_status_code} статус-код, "
                                                              f"получен {response.status_code}")
        response_error = response.json().get("err")
        assert response_error == "Task name invalid", f"Ошибка ответа: {response_error}"
        return response_error
