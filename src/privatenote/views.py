import os

from flask import request, render_template

from privatenote import app
from .models import db, Note
from .utils import generate_unique_url, get_expiration_date

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    # show the index page 'index.html'
    return render_template('index.html')


@app.route('/create-note', methods=['POST'])
def create_note():
    if request.method == "POST":
        note_content = request.form['content']
        new_url = generate_unique_url()
        days = int(os.environ.get("NOTE_EXPIRATION", default=10))
        expiration_date = get_expiration_date(days)
        new_note = Note(content=note_content, unique_url=new_url, date_expiration=expiration_date)

        try:
            new_note.save()
            return str(new_url)
        except Exception as e:
            print(e)
            return "There was an issue adding your Note!"


@app.route('/note-warn/<string:u_url>', methods=['GET'])
def note_warn(u_url):
    note = Note.objects.get(unique_url=u_url)
    # show the warning page 'warning.html'
    return render_template('warning.html', note=note)


@app.route('/note/<string:u_url>', methods=['GET'])
def show_note(u_url):
    # show note and then delete it
    try:
        note = Note.objects.get(unique_url=u_url)
        print("dict: ", note.__dict__)
        note_content = note.content
        note.delete()
        return note_content

    except Exception as e:
        print(e)
        return "Note does not exist!"
