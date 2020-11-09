from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Todo

#class TodoCheck :
 #   def __init__(self, message) :
  #      self.message = message
#
 #   def __call__( self, form, field ) :
  #     all_todos = Todo.query.all()
   #    for todo in all_todos :
    #       if todo.task == field.data :
     #          raise ValidationError( self.message )

class TodoForm( FlaskForm ) :
    task = StringField( 'Task',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField( 'Add Todo' )

    def validate_task( self, task ) :
        all_todos = Todo.query.all()
        if task.data in all_todos:
            raise ValidationError( 'This task already exists')

class OrderForm( FlaskForm ) :
    order = SelectField( 'Order',
        choices = [
            ("old", "Oldest"),
            ("new", "Newest"),
            ("complete", "Completed"),
            ("incomplete", "Incompleted")
        ]
    )

    submit = SubmitField( 'Order' )
