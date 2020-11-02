from flask import Flask


app = Flask(__name__)

print('等会谁（哪个包或模块）在使用我：',__name__)

from app import routes


