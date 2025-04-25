import os

BASE_DIR = os.path.dirname(__file__)

print(BASE_DIR)

# Init database
from .database import DatabaseClient
db_client = DatabaseClient()


from .main import app
