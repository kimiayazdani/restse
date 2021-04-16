import string
from random import random

from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
tokens = {}


class Todo(db.Model):
    username = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String(11), nullable=False)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    new_user = Todo(username=data['username'], password=data['password'], email=data['email'], number=data['number'])

    try:
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'Success'}, HTTPStatus.CREATED

    except:
        return {'message': 'Error: bad request'}, HTTPStatus.BAD_REQUEST


@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    data = request.json
    if data['token'] != token['username']:
        return {'message': 'Error'}, HTTPStatus.Unauthorized
    if request.method == 'POST':
        user = Todo.query.get_or_404(id)
        user.password = request.form['password']
        user.email = request.form['email']
        user.number = request.form['number']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return {'message': 'Cannot change user data'}, HTTPStatus.BAD_REQUEST



@app.route('/show_user/<int:id>', methods=['GET'])
def show_user(id):
    data = request.json
    if data['token'] != token['username']:
        return {'message': 'Error'}, HTTPStatus.Unauthorized

    if request.method == 'GET':
        try:
            user = Todo.query.filter_by(id=id)
            return {'message': 'Success', 'user': user}, HTTPStatus.OK
        except:
            return {'message': 'Error'}, HTTPStatus.NOT_FOUND


@app.route('/signin', methods=['POST'])
def signin():
    data = request.json

    now = datetime.date.today()
    difference1 = datetime.timedelta(days=1)
    try:
        user = Todo.query.filter_by(username=data['username'], password=data['password'])
        token[username] = (''.join(random.choice(string.ascii_lowercase)), now + difference1)
        return {'message': "success", 'token': token[username][0]}, HTTPStatus.OK
    except:
        return {'message': 'Bad fields'}, HTTPStatus.BAD_REQUEST


if __name__ == "__main__":
    app.run(debug=False)
