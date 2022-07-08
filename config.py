from distutils.sysconfig import PREFIX
from os import environ, path, getenv
from dotenv import load_dotenv
import os

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    UPLOAD_FOLDER = getenv('UPLOAD_FOLDER')
    FLASK_DEBUG = getenv('FLASK_DEBUG')

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_USERNAME = getenv('DB_USERNAME')
    DB_PASSWORD = getenv('DB_PASSWORD')
    DB_HOST = getenv('DB_HOST')
    DB_PORT = getenv('DB_PORT')
    DB_DBNAME = getenv('DB_DBNAME')
    PREFIX = getenv('PREFIX')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DBNAME}'
