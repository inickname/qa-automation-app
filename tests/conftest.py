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

    yield _task_data


@pytest.fixture()
def delete_manager(auth_session):
    task_id_pool = []

    yield task_id_pool

    for task_id in task_id_pool:
        dede = TaskApiClient(auth_session)
        dede.delete_task(task_id)
