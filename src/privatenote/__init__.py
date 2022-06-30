import os

from flask import Flask

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': os.environ.get('DB_NAME', default='my_notes'),
    'host': 'localhost',
    'port': 27017,
    'username': os.environ.get('DB_USER', default='mongouser'),
    'password': os.environ.get('DB_PASSWORD', default='12345678')
}

import privatenote.views
