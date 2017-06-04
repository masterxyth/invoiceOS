import sys

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import login_user


from dbhelper import DBHelper
from forms import LoginForm
from forms import RegistrationForm
from passwordhelper import PasswordHelper
from user import User

DB = DBHelper()
PH = PasswordHelper()
app = Flask(__name__)



app.secret_key = 'S/EgFas2Cfk/BPlHVTTpYZV4vH/qN3o4Zn/h0AKE57jyE9/3dtUJJqIBBGWZhq1A+Dh8fwI7qX0cTuAp1XRc9pb/6g+xoi/zlImH'

@app.route("/")
def home():
    registrationform= RegistrationForm()
    return render_template("home.html",registrationform=registrationform)

# If validated, register user with their email, hashes their password with salt

@app.route("/register", methods=["POST"])
def register():
    form = RegistrationForm(request.form)
    if form.validate():
        if DB.get_user(form.email.data):
            form.email.errors.append('Email address is already registered')
            return render_template('home.html', registrationform=form)
        salt = PH.get_salt()
        hashed = PH.get_hash(form.password.data + salt)
        DB.create_user(form.email.data, salt, hashed)
        return render_template('home.html', registrationform=form, onloadmessage="Registration success. Please login.")
    return render_template('home.html', registrationform=form)

@app.route('/login', methods=["POST"])
def login():
    form = LoginForm(request.form)
    if form.validate():
        stored_user = DB.get_user(form.loginemail.data)
        if stored_user and PH.validate_password(form.loginpassword.data, stored_user['salt'], stored_user['hashed']):
            user = User(form.login.data)
            login_user(user, remember=True)
            return redirect(url_for('account'))
        form.loginemail.errors.append('Email or password invalid')
    return render_template('home.html', loginform=form, registrationform=RegistrationForm())

@app.route('/account', methods=['POST'])
def account():
    return redirect(url_for('home.html'))



if __name__ == '__main__':
    app.run(port=5000, debug=True)
