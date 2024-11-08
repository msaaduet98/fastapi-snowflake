import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "snowflake://<your_connection_string>")


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(Config):
    pass


class TestConfig(Config):
    pass


class IntegrationTestConfig(Config):
    pass


class ProductionConfig(Config):
    pass
