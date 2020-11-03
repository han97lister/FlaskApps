from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy( app )

class Orders( db.Model ) :
    id = db.Column( db.Integer, primary_key = True )
    product_id = db.Column( db.Integer, db.ForeignKey('products.id'), nullable= False )
    customer_id = db.Column( db.Integer, db.ForeignKey('customers.id'), nullable = False )

class Products( db.Model ) :
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String(30), nullable = False, unique = True )
    price = db.Column( db.Integer, nullable = False )
    orders = db.relationship( 'Orders', backref = 'products' )

class Customers( db.Model ) :
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String(30), nullable = False )
    email = db.Column( db.String(30), nullable = False, unique = True )
    orders = db.relationship( 'Orders', backref = 'customers' )
