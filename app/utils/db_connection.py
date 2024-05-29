import pymongo
from utils.logging_config import logging
import os
from dotenv import load_dotenv

env_path = os.path.dirname(os.getcwd()) + "/app"
load_dotenv(os.path.join(env_path, ".env"))
ENVIRONMENT = os.getenv("ENVIRONMENT")
logging.debug(f"Creating the pymongo connection")
client = pymongo.MongoClient(os.getenv("DB_URI"))
aiq_db = client[os.getenv("DB_NAME")]
