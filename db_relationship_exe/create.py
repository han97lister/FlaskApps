from app import db, Orders, Customers, Products

db.create_all()

hanz = Customers( name = 'Hannah', email = 'han@hanz.com' )

phone = Products( name = 'IPhone100', price = 5000.00 )

db.session.add( hanz )
db.session.add( phone )
db.session.commit()

order_product = Orders( product_id = phone.id, customer_id = hanz.id )

db.session.add( order_phone )
db.session.commit()
