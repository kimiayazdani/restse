from flask import Flask
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
    



if __name__ == "__main__":
    app.run(debug=False)
