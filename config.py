
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tenfavds:RRFH1E7wEEu_sGcYLNIi-f1frn3kmSbg@bubble.db.elephantsql.com/tenfavds'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

jwt = JWTManager(app)


