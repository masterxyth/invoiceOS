import sys

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import login_user
from flask_login import LoginManager
from flask_login import login_required


from dbhelper import DBHelper
from forms import LoginForm
from forms import RegistrationForm
from passwordhelper import PasswordHelper
from user import User

DB = DBHelper()
PH = PasswordHelper()

app = Flask(__name__)
app.secret_key = 'S/EgFas2Cfk/BPlHVTTpYZV4vH/qN3o4Zn/h0AKE57jyE9/3dtUJJqIBBGWZhq1A+Dh8fwI7qX0cTuAp1XRc9pb/6g+xoi/zlImH'
login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route("/")
def home():
    registrationform= RegistrationForm()
    return render_template("home.html",registrationform=registrationform, loginform=LoginForm())

# If validated, register user with their email, hashes their password with salt

@app.route("/register", methods=["POST"])
def register():
    form = RegistrationForm(request.form)
    if form.validate():
        if DB.get_user(form.email.data):
            form.email.errors.append('Email address is already registered')
            return render_template('home.html', registrationform=form, loginform=LoginForm())
        salt = PH.get_salt()
        hashed = PH.get_hash(form.password.data + salt)
        DB.create_user(form.email.data, salt, hashed)
        return render_template('home.html', loginform=LoginForm(), registrationform=form, onloadmessage="Registration success. Please login.")
    return render_template('home.html', registrationform=form, loginform=LoginForm())

@app.route('/login', methods=["POST"])
def login():
    form = LoginForm(request.form)
    if form.validate():
        stored_user = DB.get_user(form.email.data)
        if stored_user and PH.validate_password(form.password.data, stored_user[0]['salt'], stored_user[0]['hashed']):
            user = User(form.email.data)
            login_user(user, remember=True)
            return redirect(url_for('account'))
        form.email.errors.append('Email or password invalid')
    return render_template('home.html', loginform=form, registrationform=RegistrationForm())


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


@app.route('/account')
@login_required
def account():
    return render_template('account.html')

@app.route('/create_company')
@login_required
def create_company():
    #Create company code here
    return

@app.route('/create_indent')
@login_required
def create_indent():
    #Indent code here
    return

@app.route('/generate')
@login_required
def generate():
    #Indent generation
    return

#Get Old Indent

#Edit Indent w/Logs

#Save Edits

#Print Indent

if __name__ == '__main__':
    app.run(port=5000, debug=True)
