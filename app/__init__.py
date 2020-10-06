from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_sec_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''ninky@localhost/user_profile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

print("db created")

