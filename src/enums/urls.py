from enum import Enum
from dotenv import load_dotenv

load_dotenv()


class Url(Enum):
    BASE_URL = "https://api.clickup.com"
