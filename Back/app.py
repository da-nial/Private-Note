from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# TODO: connect to MongoDB
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)


class Note(db.Model):
    unique_url = db.Column(db.String(300), primary_key=True, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    # TODO: this field should be filled from config file
    date_expiration = db.Column(db.DateTime)

    def __repr__(self) -> str:
        rep_str = "Note: " + self.unique_url + "--- Content: " + self.content
        return rep_str


# TODO: complete this function
def generate_unique_url():
    return 'url'


@app.route('/', methods=['GET'])
def index():
    # TODO: show the index page
    return "Index page"


@app.route('/delete/<string:u_url>')
def delete(u_url):
    note_to_delete = Note.query.get_or_404(u_url)

    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue deleting your Note!"


@app.route('/create-note', methods=['POST'])
def create_note():
    if request.method == "POST":
        note_content = request.form['content']
        new_url = generate_unique_url()
        # expiration_date = TODO: read from config file
        new_note = Note(content=note_content, unique_url=new_url)

        try:
            db.session.add(new_note)
            db.session.commit()
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
    note = Note.query.get_or_404(u_url)
    return note.__repr__()


if __name__ == "__main__":
    app.run(debug=True)
