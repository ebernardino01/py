import os
os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'


# Configuration class
class Config(object):
    # authentication
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-flaskapp'
    TOKEN_TIME = 800
    BYTE_LENGTH = 24
    BYTE_LENGTH_ID = 18
    BYTE_LENGTH_SECRET = 36

    # fields
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 100
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 32
    SERVICE_MIN_LENGTH = 2
    SERVICE_MAX_LENGTH = 255

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2:///psqlappdb'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # json schema validator
    JSONSCHEMA_ROOT = 'schemas'

    # route url
    API_PROTOCOL = 'http://'
    API_AUTH_HOST = 'localhost'
    API_AUTH_PORT = '5001'
    API_BILL_HOST = 'localhost'
    API_BILL_PORT = '5002'
    API_FILEMGMT_HOST = 'localhost'
    API_FILEMGMT_PORT = '5003'
    API_OAUTH_HOST = 'localhost'
    API_OAUTH_PORT = '5003'

    # rest api
    REST_CONTENT_TYPE = 'application/json'

    # datacenter
    DC_SEQ_DEFAULT = 1234567
    DC_LOCATION = 'DC0001'

    # file management
    HOME_DIR = '/Users/Shared/flaskapphome/dir'
    DOWNLOAD_DIR = 'REPOSITORY'
    READ_SIZE = 8192

    # marshmallow
    # PAGE_SIZE = 10

    # oauth
    OAUTH2_REFRESH_TOKEN_GENERATOR = True

    # redis
    REDIS_URL = 'redis:///localhost:6379/0'
    REDIS_CHANNEL = 'redis-api-channel'

    # flask-executor
    EXECUTOR_TYPE = 'thread'
    EXECUTOR_MAX_WORKERS = 10

    # flask-apscheduler
    SCHEDULER_API_ENABLED = True
