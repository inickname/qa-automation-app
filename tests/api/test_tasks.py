import pytest

from src.api_clients.task_api_client import TaskApiClient
from src.scenarios.task_scenarios import TaskScenarios
from tests.conftest import delete_manager


class TestTasks:
    def test_create_task_and_check(self, auth_session, delete_manager, task_data, list_id="901519603511"):
        """
        Сценарий: создать и проверить task.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.create_task_and_check(delete_manager, task_data, list_id)

    def test_get_and_verify_task_exist(self, auth_session, delete_manager, task_data, list_id="901519603511"):
        """
        Сценарий: получить task и проверить, что ответ не пуст.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.get_and_verify_task_exist(delete_manager, task_data, list_id)

    @pytest.mark.parametrize("invalid_task_data, expected_status_code", [
        ({'name': ''}, 400),
        ({"name": None}, 400),
        ({"name": 0}, 400),
        ({"description": "Description"}, 400)
    ])
    def test_create_task_negative(self, auth_session, invalid_task_data, expected_status_code, list_id="901519603511"):
        """
        Сценарий: создать task с разными наборами невалидных данных,
        чтобы убедиться, что система правильно обрабатывает ошибки.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.create_task_negative(list_id, invalid_task_data, expected_status_code)
