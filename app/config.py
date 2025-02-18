import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    MONGO_URL = os.getenv('MONGODB_URL')
    MONGO_DB = os.getenv('MONGODB_DB_NAME')
   