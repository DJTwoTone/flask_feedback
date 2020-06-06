from flask import Flask
from models import db, connect_db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'idonthavetolistentoyou'
app.config['DEBUG_TB_INTERCEPTS_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


