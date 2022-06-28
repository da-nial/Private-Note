from flask import Flask, request, redirect
from flask_mongoengine import MongoEngine
from mongoengine import *
from datetime import datetime, timedelta
import os
import json
import uuid

app = Flask(__name__)
# connect to MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'my_notes',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class Note(db.Document):
    unique_url = StringField(primary_key=True, required=True)
    content = StringField(required=True)
    # this field should be filled from config file
    date_expiration = DateTimeField(default=30)

    def __repr__(self) -> str:
        rep_str = "Note: " + self.unique_url + "--- Content: " + self.content
        return rep_str


# review this function
def generate_unique_url():
    return str(uuid.uuid4())


def get_expiration_date(day):
    ini_time_for_now = datetime.now()
    future_date_after_n_days = ini_time_for_now + timedelta(days=day)
    return future_date_after_n_days


@app.route('/', methods=['GET'])
def index():
    # TODO: show the index page
    return "Index page"


@app.route('/create-note', methods=['POST'])
def create_note():
    if request.method == "POST":
        note_content = request.json["content"]
        new_url = generate_unique_url()
        days = os.environ.get("note-expiration", default=10)
        expiration_date = get_expiration_date(days)
        new_note = Note(content=note_content, unique_url=new_url, date_expiration=expiration_date)

        try:
            new_note.save()
            # TODO: return created url to the client
            return str(new_url)
        except Exception as e:
            print(e)
            return "There was an issue adding your Note!"


@app.route('/note-warn/<string:u_url>', methods=['GET'])
def note_warn(u_url):
    # TODO: show the warning page
    return "warning page for: " + u_url


@app.route('/note/<string:u_url>', methods=['GET'])
def show_note(u_url):
    # TODO: show note and then delete it
    note = Note.objects(unique_url=u_url)
    return note.__repr__()


@app.route('/delete/<string:u_url>')
def delete(u_url):
    note_to_delete = Note.objects(unique_url=u_url)

    try:
        note_to_delete.delete()
        return redirect('/')
    except Exception as e:
        print(e)
        return "There was an issue deleting your Note!"


if __name__ == "__main__":
    app.run(debug=True)
