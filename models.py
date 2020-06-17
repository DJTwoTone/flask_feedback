from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """A model for our users"""

    __tablename__ = 'users'

    username = db.Column(db.String(20),
                            primary_key=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50),
                        nullable=False,
                        unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    feedback = db.relationship('Feedback')
    

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """register users with hashed passwords"""

        hashed = bcrypt.generate_password_hash(password)

        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, password):
        """Validates user and password """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False    

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

class Feedback(db.Model):
    """A model to give feedback"""

    __tablename__ = 'feedback'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=False)
    user = db.Column(db.String, db.ForeignKey('users.username'))


    def edit(self, title, content):
        self.title = title
        self.content = content
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

