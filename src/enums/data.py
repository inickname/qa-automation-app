from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()


class AuthData(Enum):
    CLICKUP_EMAIL = os.getenv("CLICKUP_EMAIL")
    CLICKUP_PASSWORD = os.getenv("CLICKUP_PASSWORD")
