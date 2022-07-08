from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_login import LoginManager
from sqlalchemy.ext.declarative import declarative_base

from flask_migrate import Migrate
migrate = Migrate(compare_type=True)

db = SQLAlchemy()
Base = declarative_base()
