from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db?timeout=10'

app.config['SECRET_KEY']='cd9c6a566cd2ade8d4aa9d58'
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10 
db = SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view='login_page'
login_manager.login_message_category="info"
bcrypt=Bcrypt(app)

from market import routes  
