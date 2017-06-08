from flask import Flask, render_template, json, request
#from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from datetime import datetime
from pytz import timezone
import pytz




## DB Connection

"""

mysql = MySQL()

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Mc$pacejam101'
app.config['MYSQL_DATABASE_DB'] = 'indentify'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



conn = mysql.connect()
cursor = conn.cursor()
"""

app = Flask(__name__)


## App Home
@app.route('/')

def main():
	return render_template('home.html')


## New User Signup Page Render

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


#New User Signup Code
@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	_hashed_password = generate_password_hash(_password)
	cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
	data = cursor.fetchall()

	if len(data) is 0:
		conn.commit()
		return json.dumps({'message':'User created successfully !'})
	else:
		return json.dumps({'error':str(data[0])})




## Login Authentication Code
@app.route("/SignIn")
def Authenticate():

    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from user where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

## Form Sending Code

@app.route('/send', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		indentid = request.form['indent-id']
		BuyerName = request.form['buyer-name']
		BuyerAddress1 = request.form['buyer-address1']
		BuyerAddress2 = request.form['buyer-address2']
		BuyerCity = request.form['buyer-city']
		BuyerCountry = request.form['buyer-country']
		SellerName = request.form['seller-name']
		SellerAddress1 = request.form['seller-address1']
		SellerAddress2 = request.form['seller-address2']
		SellerCity = request.form['seller-city']
		SellerCountry = request.form['seller-country']
		ProductName = request.form['product-name']
		qty = int(request.form['qty'])
		qtype = request.form['qtype']
		rate = int(request.form['rate'])
		pkg = request.form['pkg']
		total = rate*qty
		origin = request.form['origin']
		ContainerType = request.form['container-type']
		PaymentTerm = request.form['payment-term']
		ShipPort = request.form['ship-port']
		PortDays = request.form['port-days']
		NegoCity = request.form['nego-city']
		RouteDetail = request.form['route-detail']
		insurance = request.form['insurance']

		return render_template('dynamicIndent.html', total=total, ShipPort=ShipPort, insurance=insurance, pkg=pkg, origin=origin, indentid=indentid, qtype=qtype, BuyerName=BuyerName, BuyerAddress1=BuyerAddress1,BuyerAddress2=BuyerAddress2, BuyerCity=BuyerCity, BuyerCountry=BuyerCountry,SellerName=SellerName,SellerAddress1=SellerAddress1,SellerAddress2=SellerAddress2, SellerCity=SellerCity,SellerCountry=SellerCountry,ProductName=ProductName,qty=qty,ContainerType=ContainerType,rate=rate,PaymentTerm=PaymentTerm, PortDays=PortDays, NegoCity=NegoCity,RouteDetail=RouteDetail)


	return render_template('form.html')

if __name__ == "__main__":
	app.run()
