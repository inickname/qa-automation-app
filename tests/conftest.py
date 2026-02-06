import pytest

import requests

from src.api_clients.task_api_client import TaskApiClient
from src.data_models.task_request_data_model import TaskDataModel
from src.enums.headers import Headers

HEADERS = Headers.HEADERS.value


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    return session


@pytest.fixture()
def task_data():
    def _task_data():
        task = TaskDataModel.create_task_data()

        return task

    return _task_data


@pytest.fixture()
def delete_manager(auth_session):
    task_api_client = TaskApiClient(auth_session)
    task_id_pool = []

    yield task_id_pool

    for task_id in task_id_pool:
        task_api_client.delete_task(task_id)

        get_tasks_response = task_api_client.get_tasks("901519603511").json()
        task_ids = [task.get('id') for task in get_tasks_response.get('tasks', [])]
        assert task_id not in task_ids, "ID созданного task найден в списке tasks после удаления."
