import os
from dotenv import load_dotenv

load_dotenv()

conn_string = ''

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", conn_string)


class LocalConfig(Config):
    pass


class TestConfig(Config):
    pass


class IntegrationTestConfig(Config):
    pass


class ProductionConfig(Config):
    pass
