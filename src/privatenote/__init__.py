import os

from flask import Flask

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('MONGO_HOST', '127.0.0.1'),
    'port': int(os.environ.get('MONGO_PORT', 27017)),
    'db': os.environ.get('MONGO_INITDB_DATABASE', default='notes'),
    'username': os.environ.get('MONGO_INITDB_ROOT_USERNAME', default='myroot'),
    'password': os.environ.get('MONGO_INITDB_ROOT_PASSWORD', default='my-super-secret-password')
}

print(f"MONGODB_SETTINGS: {app.config['MONGODB_SETTINGS']}")

import privatenote.views

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=int(os.environ.get('PORT', default=5000)))
