from flask import Flask
from flask_sqlalchemy import SQLAlchemy, insert 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    username = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    number = db.Coumn(db.String(11), nullable=False)



@app.route('/')
def index():
    return "something"


if __name__ == "__main__":
    app.run(debug=False)
