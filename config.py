import os
from dotenv import find_dotenv, load_dotenv

class Config(object):
    env = os.environ.get('DEPLOY_ENVIRONMENT', None)
    if env == 'DEVELOPMENT':
        env_file = find_dotenv(filename='.env.dev')
    elif env == 'PRODUCTION':
        env_file = find_dotenv(filename='.env.prod')
    else:
        env_file = find_dotenv(filename='.env')
    load_dotenv(env_file)

    DEBUG=os.environ.get('DEBUG', False)
    SECRET_KEY=os.environ.get('APP_SECRET', 'D3faultS3cr3t!')
    DB_HOST=os.environ.get('DB_HOST','127.0.0.1')
    DB_PORT=os.environ.get('DB_PORT', 5432)
    DB_DATABASE=os.environ.get('DB_DATABASE','127.0.0.1')
    DB_USER=os.environ.get('DB_USER', 'todoapp')
    DB_PASSWORD=os.environ.get('DB_PASSWORD','password')
    SQLALCHEMY_DATABASE_URI="postgresql://{0}:{1}@{2}:{3}/{4}".format(
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_DATABASE
        )
    SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)