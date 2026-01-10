import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()


class Headers(Enum):
    HEADERS = {
        "accept": "application/json",
        "Authorization": os.getenv("CLICKUP_API_KEY")
    }
