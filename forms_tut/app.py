from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField, DecimalField

app = Flask(__name__)

app.config['SECRET_KEY'] = 's3cret$hh'

class BasicForm( FlaskForm ) :
    first_name = StringField( 'First Name' )
    last_name = StringField( 'Last Name' )
    age = IntegerField( 'Age' )
    favourite_colour = SelectField( 'Colour choice', choices=[( 'Blue', 'blue' ), ( 'Purple', 'purple' )] )
    date = DateField()
    price_of_your_shoes = DecimalField()
    submit = SubmitField( 'Add Name' )

@app.route( '/', methods=[ 'GET', 'POST' ])
@app.route( '/home', methods=[ 'GET', 'POST' ])
def register() :
    error = ""
    form = BasicForm()

    if request.method == 'POST' :
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0 :
            error = "Please supply both first and last name"
        else :
            return 'thank-you ' + str(first_name)

    return render_template( 'home.html', form=form, message=error )

if __name__=='__main__' :
    app.run( debug=True, host='0.0.0.0' )
