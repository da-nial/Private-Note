from flask import Flask, render_template, request, redirect, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import *
import json
from datetime import datetime
import uuid

app = Flask(__name__)
# TODO: connect to MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'my_notes',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class Note(db.Document):
    unique_url = StringField(primary_key=True, required=True)
    # unique_url = db.Column(db.String(300), primary_key=True, nullable=False)
    content = StringField(required=True)
    # content = db.Column(db.String(500), nullable=False)
    # TODO: this field should be filled from config file
    date_expiration = DateTimeField()
    # date_expiration = db.Column(db.DateTime)

    def __repr__(self) -> str:
        rep_str = "Note: " + self.unique_url + "--- Content: " + self.content
        return rep_str


# TODO: review this function
def generate_unique_url():
    return uuid.uuid4()


@app.route('/', methods=['GET'])
def index():
    # TODO: show the index page
    return "Index page"


@app.route('/create-note', methods=['POST'])
def create_note():
    if request.method == "POST":
        note_content = request.form['content']
        new_url = generate_unique_url()
        # expiration_date = TODO: read from config file
        new_note = Note(content=note_content, unique_url=new_url)

        try:
            new_note.save()
            # db.session.add(new_note)
            # db.session.commit()
            # TODO: return created url to the client
            return new_url
        except:
            return "There was an issue adding your Note!"


@app.route('/note/warn/<string:u_url>', methods=['GET'])
def note_warn(u_url):
    # TODO: show the warning page
    return "warning page for: " + u_url


@app.route('/note/<string:u_url>', methods=['GET'])
def show_note(u_url):
    # TODO: show note and then delete it
    note = Note.objects(unique_url=u_url)
    # note = Note.query.get_or_404(u_url)
    return note.__repr__()


@app.route('/delete/<string:u_url>')
def delete(u_url):
    note_to_delete = Note.objects(unique_url=u_url)
    # note_to_delete = Note.query.get_or_404(u_url)

    try:
        note_to_delete.delete()
        # db.session.delete(note_to_delete)
        # db.session.commit()
        return redirect('/')
    except:
        return "There was an issue deleting your Note!"


if __name__ == "__main__":
    app.run(debug=True)
