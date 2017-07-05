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
from flask_login import current_user


from dbhelper import DBHelper
from forms import CompanyForm
from forms import IndentForm
from forms import LoginForm
from forms import RegistrationForm
from passwordhelper import PasswordHelper
from user import User

DB = DBHelper()
PH = PasswordHelper()

app = Flask(__name__)
app.secret_key = ''
login_manager = LoginManager(app)
login_manager.init_app(app)

#rendering the homepage with the Registration From
@app.route("/")
def home():
    registrationform= RegistrationForm()
    return render_template("home.html",registrationform=registrationform, loginform=LoginForm())

""" Once user clicks register, system checks if information provided is correct; Checks if user already exists: gives error.
    Otherwise, it gets a salt, creates a hash with salth, which it uses to create a new user with their email, salt, and hash.
    If registration is successful, provides user with an affirmative message.
"""

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
            return redirect(url_for('launch'))
        form.email.errors.append('Email or password invalid')
    return render_template('home.html', loginform=form, registrationform=RegistrationForm())

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)

@app.route('/launch')
@login_required
def launch():
    cname = 'Pakland Chemicals'
    return render_template('launch.html')
    #Update Company Information
    # Create an Indent
    #View Past Indents
    return render_template('dash.html')

@app.route('/company')
@login_required
def company():
    return render_template('create-company.html', companyform=CompanyForm())

@app.route('/create_company', methods=['POST'])
@login_required
def create_company():
    form = CompanyForm(request.form)
    stored_user = DB.get_user(current_user.get_id())
    if DB.get_company(stored_user[0]['id']):
        data = DB.get_company(stored_user[0]['id'])
        return render_template ('create-company.html', data = data, companyform=form)
    elif form.validate():
        DB.create_company(stored_user[0]['id'], form.company_name.data, form.address1.data, form.address2.data, form.phone.data, form.fax.data, form.email.data)
        return render_template('launch.html', onloadmessage='Company Information Successfully Updated.')
    return render_template('create-company.html', companyform=form)


@app.route('/indent')
@login_required
def indent():
    return render_template('create-indent.html', indentform=IndentForm())

@app.route('/create_indent')
@login_required
def create_indent():
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
