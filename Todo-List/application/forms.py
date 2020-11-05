from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from application.models import Todo

class TodoCheck :
    def __init__(self, message) :
        self.message = message

    def __call__( self, form, field ) :
       all_todos = Todo.query.all()
       for todo in all_todos :
           if todo.task == field.data :
               raise ValidationError( self.message )

class TodoForm( FlaskForm ) :
    task = StringField( 'Task', validators=[
            DataRequired(),
            TodoCheck( message= "This task already exists" ) ])
    submit = SubmitField( 'Add Todo' )
