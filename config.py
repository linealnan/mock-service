import os
import uuid


class BaseConfig:
    HOST = '0.0.0.0'
    LOCAL_HOST = os.environ.get('LOCAL_HOST')
    LOCAL_PORT = os.environ.get('LOCAL_PORT')

    DEBUG = False
    TESTING = False
    SECRET_KEY = str(uuid.uuid4())
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    JSON_SORT_KEYS = False

    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class DevelopmentConfig(BaseConfig):
    PORT = 5001


class TestingConfig(BaseConfig):
    PORT = 5001


class ProductionConfig(BaseConfig):
    HOST = '0.0.0.0'
    PORT = 5001
