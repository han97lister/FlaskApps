from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField # We will only use StringField and SubmitField in our simple form.
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY' #Configure a secret key for CSRF protection.

class UserCheck :
    def __init__( self, banned, message=None ) :
        self.banned = banned
        if not message :
            message = 'Please choose another username'
        self.message = message

    def __call__( self, form, field ) :
        if field.data.lower() in ( word.lower() for word in self.banned ) :
            raise ValidationError( self.message )

class CharacterCheck :
    def __init__( self, char, message ) :
        self.char = char
        self.message = message

    def __call__( self, form, field ) :
        for letter in  field.data :
            for char in self.char :
                if letter == char :
                    raise ValidationError( self.message )

class MyForm( FlaskForm ) :
    username = StringField( 'Username', validators=[
        DataRequired(),
        UserCheck( message="Pick a better username", banned = [ 'root', 'admin', 'sys' ]),
        CharacterCheck( message="Don't use special characters", char = ['!', '£', '$', '%'] ),
        Length( min=2, max=15 )
        ])
    submit = SubmitField( 'Sign up' )

@app.route( '/', methods=[ 'GET', 'POST' ] )
def postName() :
    form = MyForm()
    if form.validate_on_submit() :
        username = form.username.data
        return render_template( 'home.html', form = form, username = username )
    else :
        return render_template( 'home.html', form = form, username = "" )


if __name__=='__main__' :
    app.run( debug=True, host='0.0.0.0' )

