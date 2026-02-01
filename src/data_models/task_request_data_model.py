from faker import Faker
from pydantic import BaseModel

faker = Faker()


class TaskDataModel(BaseModel):
    name: str

    @staticmethod
    def create_task_data():
        return TaskDataModel(
            name=faker.text(max_nb_chars=10)
        )
