from flask import Flask, redirect, render_template, flash, session
from models import db, connect_db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'idonthavetolistentoyou'
app.config['DEBUG_TB_INTERCEPTS_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)
        db.session.add(user)
        db.session.commit()
        

        session["username"] = user.username
        
        return redirect(f'users/{user.username}')
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)


        if user:
            session['username'] = user.username
            return redirect(f'users/{user.username}')
        else:
            form.username.errors = ["Incorrect name/password"]

    return render_template('login.html', form=form)

@app.route("/secret")
def secret():
    if "username" not in session:
        flash("You must register to see the secret!")
        redirect('/')

    else:
        return render_template("secret.html")



@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

@app.route("/users/<username>")
def user_info(username):
    if username != session['username']:
        flash("You must be logged in")
        return redirect('/')

    else:
        user = User.query.filter_by(username=username).one()

        return render_template('user-info.html', user = user)


@app.route('/users/<username>/delete', methods=['POST'])
def delete_user(username):
    if username != session['username']:
        flash("You must be logged in")
        return redirect('/')

    else:
        user = User.query.get_or_404(username)
        user.delete_user()
        session.clear()

        return redirect('/')


@app.route('/users/<username>/feedback/add', methods=['GET', 'POST'])
def add_feedback(username):
    if username != session['username']:
        flash("You must be logged in")
        return redirect('/')

    else:
        form = FeedbackForm()

        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data

            

            feedback = Feedback(title=title, content=content, user=username)
            db.session.add(feedback)
            db.session.commit()

            return redirect(f'/users/{username}')

        else:

            return render_template('add-feedback-form.html', form=form)

@app.route('/feedback/<feedback_id>/update', methods=['GET', 'POST'])
def update_feedback(feedback_id):
    form = FeedbackForm()
    feedback = Feedback.query.get_or_404(feedback_id)
    
    
    if feedback.user != session['username']:
        flash("You must be logged in")
        return redirect('/')

    else:


        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data

            feedback.edit(title=title, content=content)
            return redirect(f'/users/{feedback.user}')

        else:
            form.title.data = feedback.title
            form.content.data = feedback.content
            return render_template('edit-feedback-form.html', form=form, feedback=feedback)

@app.route('/feedback/<feedbackid>/delete', methods=['POST'])
def delete_feedback(feedbackid):
    form = FeedbackForm()
    feedback = Feedback.query.get_or_404(feedbackid)
    
    if feedback.user != session['username']:
        flash("You must be logged in")
        return redirect('/')

    else:

        feedback.delete()

        return redirect(f'/users/{feedback.user}')
