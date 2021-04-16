from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
tokens = {}


class Todo(db.Model):
    username = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String(11), nullable=False)


@app.route('/signup')
def signup():
    data = request.json
    new_user = Todo(username=data['username'], password=data['password'], email=data['email'], number=data['number'])

    try:
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'Success'}, HTTPStatus.CREATED

    except:
        return {'message': 'Error: bad request'}, HTTPStatus.BAD_REQUEST


@app.route('/show_user', methods=['GET'])
def show_user(username):
    if request.method == 'GET':
        user = Todo.query.filter_by(username=username)

        try:
            return {'message': 'Success', 'user': user}, HTTPStatus.OK
        except:
            return {'message': 'Error'}, HTTPStatus.NOT_FOUND


if __name__ == "__main__":
    app.run(debug=False)
