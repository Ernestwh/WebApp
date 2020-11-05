from flask import Flask
from config import Config#从config模块导入Config类

from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate

from flask_login import LoginManager

import logging
from logging.handlers import RotatingFileHandler
import os



app = Flask(__name__)
app.config.from_object(Config)

if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/WebApp.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('WebApp startup')


db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象

login = LoginManager(app)
login.login_view='login'

print('等会谁（哪个包或模块）在使用我：',__name__)

from app import routes,models,errors


